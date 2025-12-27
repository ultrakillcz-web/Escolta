"""
Email notification module for security alerts
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional, Dict, List
from datetime import datetime


class EmailNotifier:
    """Send email notifications for security alerts"""

    def __init__(
        self,
        smtp_server: str = "smtp.gmail.com",
        smtp_port: int = 587,
        sender_email: Optional[str] = None,
        sender_password: Optional[str] = None,
        recipient_emails: Optional[List[str]] = None,
    ):
        """
        Initialize email notifier

        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for sender email
            recipient_emails: List of recipient email addresses
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_emails = recipient_emails or []
        self.enabled = sender_email is not None and len(self.recipient_emails) > 0

    def send_alert(self, alert: Dict) -> bool:
        """
        Send alert notification via email

        Args:
            alert: Alert dictionary with type, message, and metadata

        Returns:
            True if sent successfully, False otherwise
        """
        if not self.enabled:
            return False

        try:
            # Create message
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = ", ".join(self.recipient_emails)
            msg["Subject"] = f"Escota Security Alert: {alert['type'].upper()}"

            # Create email body
            body = f"""
Escota Security System Alert

Type: {alert['type'].upper()}
Time: {alert['timestamp']}
Message: {alert['message']}

"""
            if alert.get("metadata"):
                body += "Additional Details:\n"
                for key, value in alert["metadata"].items():
                    body += f"  {key}: {value}\n"

            msg.attach(MIMEText(body, "plain"))

            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            return True

        except Exception as e:
            print(f"Error sending email notification: {e}")
            return False

    def test_connection(self) -> bool:
        """
        Test SMTP connection

        Returns:
            True if connection successful, False otherwise
        """
        if not self.enabled:
            return False

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
            return True
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False
