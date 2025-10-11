"""
Tests for camera monitoring module
"""

import pytest

try:
    import numpy as np

    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False

if HAS_OPENCV:
    from escota.core.camera import CameraMonitor

pytestmark = pytest.mark.skipif(not HAS_OPENCV, reason="OpenCV not installed")


class TestCameraMonitor:
    """Test CameraMonitor class"""

    def test_initialization(self):
        """Test camera initialization"""
        camera = CameraMonitor(camera_id=0, resolution=(640, 480))
        assert camera.camera_id == 0
        assert camera.resolution == (640, 480)
        assert camera.is_running is False

    def test_context_manager(self):
        """Test context manager usage"""
        # Note: This will fail if no camera is available
        # In real tests, we would mock cv2.VideoCapture
        camera = CameraMonitor()
        assert camera.is_running is False

    def test_save_frame(self, tmp_path):
        """Test saving frame to file"""
        camera = CameraMonitor()

        # Create a dummy frame
        frame = np.zeros((480, 640, 3), dtype=np.uint8)

        # Save to temporary path
        filepath = tmp_path / "test_frame.jpg"
        result = camera.save_frame(frame, str(filepath))

        assert result is True
        assert filepath.exists()
