"""
Camera monitoring module for security surveillance
"""

try:
    import cv2
    import numpy as np

    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False

from typing import Optional, Tuple
from datetime import datetime


class CameraMonitor:
    """Monitor video feed from camera for security surveillance"""

    def __init__(self, camera_id: int = 0, resolution: Tuple[int, int] = (640, 480)):
        """
        Initialize camera monitor

        Args:
            camera_id: Camera device ID (0 for default camera)
            resolution: Video resolution as (width, height)
        """
        if not HAS_OPENCV:
            raise ImportError(
                "OpenCV is required for camera monitoring. "
                "Install with: pip install opencv-python numpy"
            )

        self.camera_id = camera_id
        self.resolution = resolution
        self.cap: Optional["cv2.VideoCapture"] = None
        self.is_running = False

    def start(self) -> bool:
        """
        Start camera monitoring

        Returns:
            True if camera started successfully, False otherwise
        """
        try:
            self.cap = cv2.VideoCapture(self.camera_id)
            if not self.cap.isOpened():
                return False

            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
            self.is_running = True
            return True
        except Exception as e:
            print(f"Error starting camera: {e}")
            return False

    def stop(self):
        """Stop camera monitoring"""
        if self.cap:
            self.cap.release()
            self.is_running = False

    def get_frame(self) -> Optional["np.ndarray"]:
        """
        Get current frame from camera

        Returns:
            Frame as numpy array or None if not available
        """
        if not self.is_running or not self.cap:
            return None

        ret, frame = self.cap.read()
        if ret:
            return frame
        return None

    def save_frame(self, frame: "np.ndarray", filepath: str) -> bool:
        """
        Save frame to file

        Args:
            frame: Frame to save
            filepath: Path to save the image

        Returns:
            True if saved successfully, False otherwise
        """
        try:
            cv2.imwrite(filepath, frame)
            return True
        except Exception as e:
            print(f"Error saving frame: {e}")
            return False

    def __enter__(self):
        """Context manager entry"""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.stop()
