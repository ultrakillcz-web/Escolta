"""
Tests for web interface module
"""

from escota.core.webui import WebInterface
from escota.core.alert import AlertSystem


class TestWebInterface:
    """Test WebInterface class"""

    def test_initialization(self):
        """Test web interface initialization"""
        alert_system = AlertSystem()
        webui = WebInterface(alert_system=alert_system, host="localhost", port=8080)

        assert webui.host == "localhost"
        assert webui.port == 8080

    def test_initialization_with_defaults(self):
        """Test web interface with default parameters"""
        webui = WebInterface()
        assert webui.host == "localhost"
        assert webui.port == 8080
