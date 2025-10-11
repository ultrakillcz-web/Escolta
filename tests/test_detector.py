"""
Tests for motion detector module
"""

import pytest

try:
    import numpy as np

    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False

if HAS_OPENCV:
    from escota.core.detector import MotionDetector

pytestmark = pytest.mark.skipif(not HAS_OPENCV, reason="OpenCV not installed")


class TestMotionDetector:
    """Test MotionDetector class"""

    def test_initialization(self):
        """Test detector initialization"""
        detector = MotionDetector(threshold=25, min_area=500)
        assert detector.threshold == 25
        assert detector.min_area == 500
        assert detector.previous_frame is None

    def test_detect_no_motion(self):
        """Test detection with identical frames"""
        detector = MotionDetector(threshold=25, min_area=500)

        # Create identical frames
        frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
        frame2 = np.zeros((480, 640, 3), dtype=np.uint8)

        # First frame initializes previous frame
        motion1, boxes1 = detector.detect(frame1)
        assert motion1 is False
        assert len(boxes1) == 0

        # Second identical frame should detect no motion
        motion2, boxes2 = detector.detect(frame2)
        assert motion2 is False
        assert len(boxes2) == 0

    def test_detect_with_motion(self):
        """Test detection with different frames"""
        detector = MotionDetector(threshold=20, min_area=100)

        # Create first frame (black)
        frame1 = np.zeros((480, 640, 3), dtype=np.uint8)

        # Create second frame with white rectangle (motion)
        frame2 = np.zeros((480, 640, 3), dtype=np.uint8)
        frame2[100:200, 100:300] = 255  # White rectangle

        # First frame
        detector.detect(frame1)

        # Second frame should detect motion
        motion, boxes = detector.detect(frame2)
        assert motion is True
        assert len(boxes) > 0

    def test_reset(self):
        """Test detector reset"""
        detector = MotionDetector()

        # Initialize with a frame
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        detector.detect(frame)
        assert detector.previous_frame is not None

        # Reset should clear previous frame
        detector.reset()
        assert detector.previous_frame is None

    def test_draw_boxes(self):
        """Test drawing bounding boxes"""
        detector = MotionDetector()

        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        boxes = [(10, 10, 100, 100), (200, 200, 50, 50)]

        result = detector.draw_boxes(frame, boxes)

        # Result should be a copy
        assert result.shape == frame.shape
        assert not np.array_equal(result, frame)
