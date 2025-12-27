"""
Command-line interface for Escota security system
"""

import argparse
import sys
import yaml
from escota.core.camera import CameraMonitor
from escota.core.detector import MotionDetector
from escota.core.alert import AlertSystem
from escota.utils.config import load_config, get_default_config, save_config


def monitor_command(args):
    """Run security monitoring"""
    # Load configuration
    if args.config:
        config = load_config(args.config)
    else:
        config = get_default_config()

    # Initialize components
    camera_config = config.get("camera", {})
    detection_config = config.get("detection", {})
    alert_config = config.get("alerts", {})

    camera = CameraMonitor(
        camera_id=camera_config.get("id", 0),
        resolution=tuple(camera_config.get("resolution", [640, 480])),
    )

    detector = MotionDetector(
        threshold=detection_config.get("threshold", 25),
        min_area=detection_config.get("min_area", 500),
    )

    alert_system = AlertSystem(log_file=alert_config.get("log_file"))

    # Start monitoring
    print("Starting Escota security monitoring...")
    if not camera.start():
        print("Failed to start camera")
        return 1

    try:
        frame_count = 0
        while True:
            frame = camera.get_frame()
            if frame is None:
                break

            # Detect motion
            if detection_config.get("enabled", True):
                motion_detected, boxes = detector.detect(frame)

                if motion_detected:
                    print(f"Motion detected! Boxes: {len(boxes)}")
                    alert_system.create_alert(
                        "motion",
                        f"Motion detected with {len(boxes)} regions",
                        {"frame": frame_count, "boxes": boxes},
                    )

            frame_count += 1

            # Break on max frames if set
            if args.max_frames and frame_count >= args.max_frames:
                break

    except KeyboardInterrupt:
        print("\nStopping monitoring...")
    finally:
        camera.stop()

    return 0


def config_command(args):
    """Manage configuration"""
    if args.action == "init":
        config = get_default_config()
        output_path = args.output or "config/escota.yaml"
        save_config(config, output_path)
        print(f"Default configuration saved to: {output_path}")
        return 0

    elif args.action == "show":
        if args.config:
            config = load_config(args.config)
        else:
            config = get_default_config()

        print(yaml.dump(config, default_flow_style=False))
        return 0

    return 1


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Escota - Sistema de Segurança privada inteligente"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Monitor command
    monitor_parser = subparsers.add_parser("monitor", help="Start security monitoring")
    monitor_parser.add_argument("--config", "-c", help="Path to configuration file")
    monitor_parser.add_argument(
        "--max-frames", type=int, help="Maximum number of frames to process"
    )
    monitor_parser.set_defaults(func=monitor_command)

    # Config command
    config_parser = subparsers.add_parser("config", help="Manage configuration")
    config_parser.add_argument("action", choices=["init", "show"], help="Configuration action")
    config_parser.add_argument(
        "--config", "-c", help="Path to configuration file (for show action)"
    )
    config_parser.add_argument("--output", "-o", help="Output path for init action")
    config_parser.set_defaults(func=config_command)

    args = parser.parse_args()

    if hasattr(args, "func"):
        return args.func(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
