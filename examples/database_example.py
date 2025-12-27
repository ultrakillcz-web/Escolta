#!/usr/bin/env python
"""
Database Storage Example

This example demonstrates how to use database storage for alerts.
"""

from escota.core.alert import AlertSystem
from escota.core.database import AlertDatabase
import time


def main():
    print("Escota Database Storage Example")
    print("=" * 50)

    # Initialize database
    db = AlertDatabase("examples_alerts.db")
    print(f"\nDatabase initialized: examples_alerts.db")

    # Create alert system
    alert_system = AlertSystem()

    # Create some sample alerts and save to database
    print("\nCreating and saving alerts to database...")

    alerts_to_create = [
        ("motion", "Motion detected in Zone A", {"zone": "A", "confidence": 0.95}),
        (
            "intrusion",
            "Unauthorized access attempt",
            {"location": "Main Entrance", "severity": "high"},
        ),
        ("motion", "Motion detected in Zone B", {"zone": "B", "confidence": 0.87}),
        ("motion", "Motion detected in Zone C", {"zone": "C", "confidence": 0.92}),
    ]

    for alert_type, message, metadata in alerts_to_create:
        alert = alert_system.create_alert(alert_type, message, metadata)
        alert_id = db.save_alert(alert)
        print(f"  Saved alert #{alert_id}: {alert_type} - {message}")
        time.sleep(0.5)

    # Display statistics
    print(f"\n📊 Database Statistics:")
    print(f"  Total alerts: {db.get_alert_count()}")
    print(f"  Motion alerts: {db.get_alert_count('motion')}")
    print(f"  Intrusion alerts: {db.get_alert_count('intrusion')}")

    # Retrieve and display alerts
    print(f"\n📋 All Alerts from Database:")
    print("-" * 50)

    all_alerts = db.get_alerts()
    for alert in all_alerts:
        print(f"[{alert['timestamp']}] {alert['type'].upper()}: {alert['message']}")
        if alert["metadata"]:
            print(f"  Metadata: {alert['metadata']}")

    # Filter by type
    print(f"\n🔍 Motion Alerts Only:")
    print("-" * 50)

    motion_alerts = db.get_alerts(alert_type="motion")
    for alert in motion_alerts:
        print(f"[{alert['timestamp']}] {alert['message']}")

    # Pagination example
    print(f"\n📄 Latest 2 Alerts (Pagination):")
    print("-" * 50)

    recent_alerts = db.get_alerts(limit=2)
    for alert in recent_alerts:
        print(f"[{alert['timestamp']}] {alert['type'].upper()}: {alert['message']}")

    print(f"\n✅ Database example completed!")
    print(f"Database file: examples_alerts.db")


if __name__ == "__main__":
    main()
