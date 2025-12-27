"""
Tests for email notifier module
"""

from escota.core.notifier import EmailNotifier


class TestEmailNotifier:
    """Test EmailNotifier class"""

    def test_initialization_disabled(self):
        """Test notifier initialization without credentials"""
        notifier = EmailNotifier()
        assert notifier.enabled is False

    def test_initialization_enabled(self):
        """Test notifier initialization with credentials"""
        notifier = EmailNotifier(
            sender_email="test@example.com",
            sender_password="password",
            recipient_emails=["recipient@example.com"],
        )
        assert notifier.enabled is True
        assert notifier.sender_email == "test@example.com"
        assert len(notifier.recipient_emails) == 1

    def test_send_alert_disabled(self):
        """Test sending alert when disabled"""
        notifier = EmailNotifier()
        alert = {"type": "motion", "timestamp": "2024-01-01", "message": "Test"}

        result = notifier.send_alert(alert)
        assert result is False
