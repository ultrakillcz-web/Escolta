#!/usr/bin/env python
"""
Email Notification Example

This example demonstrates email notifications (configuration only).
Note: Requires actual SMTP credentials to send emails.
"""

from escota.core.alert import AlertSystem
from escota.core.notifier import EmailNotifier


def main():
    print("Escota Email Notification Example")
    print("=" * 50)

    # Initialize email notifier (disabled by default without credentials)
    notifier = EmailNotifier()

    print(f"\n📧 Email Notifier Configuration:")
    print(f"  Enabled: {notifier.enabled}")
    print(f"  SMTP Server: {notifier.smtp_server}")
    print(f"  SMTP Port: {notifier.smtp_port}")

    if not notifier.enabled:
        print(f"\n⚠️  Email notifications are disabled")
        print(f"  To enable, configure with:")
        print(f"    - Sender email address")
        print(f"    - Sender password/app password")
        print(f"    - Recipient email addresses")

    # Example with configuration (won't send without real credentials)
    print(f"\n📝 Example Configuration:")
    print(
        f"""
    notifier = EmailNotifier(
        smtp_server='smtp.gmail.com',
        smtp_port=587,
        sender_email='your-email@gmail.com',
        sender_password='your-app-password',
        recipient_emails=['recipient@example.com']
    )
    """
    )

    # Create a sample alert
    alert_system = AlertSystem()
    alert = alert_system.create_alert(
        "intrusion",
        "Critical security breach detected",
        {"location": "Main Entrance", "severity": "critical"},
    )

    print(f"\n📬 Sample Alert Created:")
    print(f"  Type: {alert['type']}")
    print(f"  Message: {alert['message']}")
    print(f"  Timestamp: {alert['timestamp']}")

    # Attempt to send (will fail without credentials)
    result = notifier.send_alert(alert)

    if result:
        print(f"\n✅ Email notification sent successfully!")
    else:
        print(f"\n❌ Email notification not sent (credentials not configured)")

    print(f"\n💡 To use email notifications:")
    print(f"  1. Enable 2-factor authentication on your Gmail account")
    print(f"  2. Generate an app password")
    print(f"  3. Configure the notifier with your credentials")
    print(f"  4. Add recipient email addresses")

    print(f"\n✅ Email notification example completed!")


if __name__ == "__main__":
    main()
