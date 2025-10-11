"""
Motion detection module for security surveillance
"""

try:
    import cv2
    import numpy as np

    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False

from typing import Optional, List, Tuple


class MotionDetector:
    """Detect motion in video frames"""

    def __init__(self, threshold: int = 25, min_area: int = 500):
        """
        Initialize motion detector

        Args:
            threshold: Threshold for detecting changes (0-255)
            min_area: Minimum area for motion detection in pixels
        """
        if not HAS_OPENCV:
            raise ImportError(
                "OpenCV is required for motion detection. "
                "Install with: pip install opencv-python numpy"
            )

        self.threshold = threshold
        self.min_area = min_area
        self.previous_frame: Optional["np.ndarray"] = None

    def detect(self, frame: "np.ndarray") -> Tuple[bool, List[Tuple[int, int, int, int]]]:
        """
        Detect motion in frame

        Args:
            frame: Current frame as numpy array

        Returns:
            Tuple of (motion_detected, bounding_boxes)
            bounding_boxes is list of (x, y, w, h) tuples
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Initialize previous frame if not set
        if self.previous_frame is None:
            self.previous_frame = gray
            return False, []

        # Compute difference between frames
        frame_delta = cv2.absdiff(self.previous_frame, gray)
        thresh = cv2.threshold(frame_delta, self.threshold, 255, cv2.THRESH_BINARY)[1]

        # Dilate the threshold image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours by area and get bounding boxes
        bounding_boxes = []
        for contour in contours:
            if cv2.contourArea(contour) < self.min_area:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            bounding_boxes.append((x, y, w, h))

        # Update previous frame
        self.previous_frame = gray

        # Return result
        motion_detected = len(bounding_boxes) > 0
        return motion_detected, bounding_boxes

    def reset(self):
        """Reset detector state"""
        self.previous_frame = None

    def draw_boxes(
        self, frame: "np.ndarray", boxes: List[Tuple[int, int, int, int]]
    ) -> "np.ndarray":
        """
        Draw bounding boxes on frame

        Args:
            frame: Frame to draw on
            boxes: List of bounding boxes (x, y, w, h)

        Returns:
            Frame with boxes drawn
        """
        result = frame.copy()
        for x, y, w, h in boxes:
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return result
