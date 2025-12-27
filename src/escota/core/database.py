"""
Database storage module for security alerts
"""

import sqlite3
import json
from typing import Optional, List, Dict
from pathlib import Path
from datetime import datetime


class AlertDatabase:
    """SQLite database for storing security alerts"""

    def __init__(self, db_path: str = "escota_alerts.db"):
        """
        Initialize alert database

        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self._init_database()

    def _init_database(self):
        """Initialize database schema"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS alerts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    type TEXT NOT NULL,
                    message TEXT NOT NULL,
                    metadata TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_timestamp 
                ON alerts(timestamp)
                """
            )
            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_type 
                ON alerts(type)
                """
            )
            conn.commit()

    def save_alert(self, alert: Dict) -> int:
        """
        Save alert to database

        Args:
            alert: Alert dictionary

        Returns:
            ID of saved alert
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO alerts (timestamp, type, message, metadata)
                VALUES (?, ?, ?, ?)
                """,
                (
                    alert["timestamp"],
                    alert["type"],
                    alert["message"],
                    json.dumps(alert.get("metadata", {})),
                ),
            )
            conn.commit()
            return cursor.lastrowid

    def get_alerts(
        self,
        alert_type: Optional[str] = None,
        limit: Optional[int] = None,
        offset: int = 0,
    ) -> List[Dict]:
        """
        Retrieve alerts from database

        Args:
            alert_type: Filter by alert type
            limit: Maximum number of alerts to return
            offset: Number of alerts to skip

        Returns:
            List of alert dictionaries
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            query = "SELECT * FROM alerts"
            params = []

            if alert_type:
                query += " WHERE type = ?"
                params.append(alert_type)

            query += " ORDER BY timestamp DESC"

            if limit:
                query += " LIMIT ? OFFSET ?"
                params.extend([limit, offset])

            cursor.execute(query, params)

            alerts = []
            for row in cursor.fetchall():
                alert = {
                    "id": row["id"],
                    "timestamp": row["timestamp"],
                    "type": row["type"],
                    "message": row["message"],
                    "metadata": json.loads(row["metadata"]) if row["metadata"] else {},
                    "created_at": row["created_at"],
                }
                alerts.append(alert)

            return alerts

    def get_alert_by_id(self, alert_id: int) -> Optional[Dict]:
        """
        Get alert by ID

        Args:
            alert_id: Alert ID

        Returns:
            Alert dictionary or None if not found
        """
        alerts = self.get_alerts(limit=1)
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alerts WHERE id = ?", (alert_id,))
            row = cursor.fetchone()

            if row:
                return {
                    "id": row["id"],
                    "timestamp": row["timestamp"],
                    "type": row["type"],
                    "message": row["message"],
                    "metadata": json.loads(row["metadata"]) if row["metadata"] else {},
                    "created_at": row["created_at"],
                }
            return None

    def get_alert_count(self, alert_type: Optional[str] = None) -> int:
        """
        Get count of alerts

        Args:
            alert_type: Filter by alert type

        Returns:
            Number of alerts
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            if alert_type:
                cursor.execute("SELECT COUNT(*) FROM alerts WHERE type = ?", (alert_type,))
            else:
                cursor.execute("SELECT COUNT(*) FROM alerts")

            return cursor.fetchone()[0]

    def delete_alert(self, alert_id: int) -> bool:
        """
        Delete alert by ID

        Args:
            alert_id: Alert ID

        Returns:
            True if deleted, False otherwise
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alerts WHERE id = ?", (alert_id,))
            conn.commit()
            return cursor.rowcount > 0

    def clear_alerts(self, alert_type: Optional[str] = None):
        """
        Clear alerts from database

        Args:
            alert_type: Clear only alerts of this type (if specified)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            if alert_type:
                cursor.execute("DELETE FROM alerts WHERE type = ?", (alert_type,))
            else:
                cursor.execute("DELETE FROM alerts")

            conn.commit()
