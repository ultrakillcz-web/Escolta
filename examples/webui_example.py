#!/usr/bin/env python
"""
Web Interface Example

This example demonstrates the web interface for viewing alerts.
"""

from escota.core.alert import AlertSystem
from escota.core.database import AlertDatabase
from escota.core.webui import WebInterface
import time


def main():
    print("Escota Web Interface Example")
    print("=" * 50)

    # Initialize components
    db = AlertDatabase("webui_alerts.db")
    alert_system = AlertSystem()

    # Create some sample alerts
    print("\nCreating sample alerts...")

    sample_alerts = [
        ("motion", "Motion detected in Front Door", {"zone": "Front", "confidence": 0.95}),
        ("motion", "Motion detected in Backyard", {"zone": "Back", "confidence": 0.88}),
        (
            "intrusion",
            "Unauthorized access detected",
            {"location": "Side Window", "severity": "high"},
        ),
        ("motion", "Motion detected in Garage", {"zone": "Garage", "confidence": 0.91}),
        (
            "intrusion",
            "Multiple failed access attempts",
            {"location": "Main Door", "attempts": 3},
        ),
    ]

    for alert_type, message, metadata in sample_alerts:
        alert = alert_system.create_alert(alert_type, message, metadata)
        db.save_alert(alert)
        print(f"  Created: {alert_type} - {message}")
        time.sleep(0.3)

    # Initialize and start web interface
    print(f"\n🌐 Starting web interface...")
    webui = WebInterface(alert_system=alert_system, database=db, host="localhost", port=8080)

    webui.start()

    print("\n" + "=" * 50)
    print("✅ Web interface is running!")
    print("=" * 50)
    print(f"\n🌐 Open your browser and navigate to:")
    print(f"   http://localhost:8080")
    print(f"\nThe page will show:")
    print(f"  • Real-time alert statistics")
    print(f"  • Recent alerts table")
    print(f"  • Auto-refresh every 5 seconds")
    print(f"\nPress Ctrl+C to stop the server...")

    try:
        # Keep the server running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n🛑 Stopping web interface...")
        webui.stop()
        print("✅ Server stopped successfully!")


if __name__ == "__main__":
    main()
