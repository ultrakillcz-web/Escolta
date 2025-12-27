#!/usr/bin/env python
"""
Basic Alert System Example

This example demonstrates the alert system without requiring camera hardware.
"""

from escota.core.alert import AlertSystem
import time


def main():
    print("Escota Alert System Example")
    print("=" * 50)

    # Initialize alert system with log file
    alert_system = AlertSystem(log_file="logs/example_alerts.log")

    # Create some sample alerts
    print("\nCreating sample alerts...")

    alert_system.create_alert(
        "motion", "Motion detected in Zone A", {"zone": "A", "confidence": 0.95}
    )

    time.sleep(1)

    alert_system.create_alert(
        "intrusion",
        "Unauthorized access attempt",
        {"location": "Main Entrance", "severity": "high"},
    )

    time.sleep(1)

    alert_system.create_alert(
        "motion", "Motion detected in Zone B", {"zone": "B", "confidence": 0.87}
    )

    # Display all alerts
    print(f"\nTotal alerts: {len(alert_system.alerts)}")
    print("\nAll Alerts:")
    print("-" * 50)

    for alert in alert_system.get_alerts():
        print(f"[{alert['timestamp']}] {alert['type'].upper()}: {alert['message']}")
        if alert["metadata"]:
            print(f"  Metadata: {alert['metadata']}")

    # Filter alerts by type
    print("\nMotion Alerts Only:")
    print("-" * 50)

    for alert in alert_system.get_alerts(alert_type="motion"):
        print(f"[{alert['timestamp']}] {alert['message']}")

    # Get latest alerts
    print("\nLatest 2 Alerts:")
    print("-" * 50)

    for alert in alert_system.get_alerts(limit=2):
        print(f"[{alert['timestamp']}] {alert['type'].upper()}: {alert['message']}")

    print(f"\nAlerts have been logged to: logs/example_alerts.log")


if __name__ == "__main__":
    main()
