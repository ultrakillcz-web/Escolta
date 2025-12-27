"""
Tests for database module
"""

from escota.core.database import AlertDatabase
import tempfile
import os


class TestAlertDatabase:
    """Test AlertDatabase class"""

    def test_initialization(self, tmp_path):
        """Test database initialization"""
        db_path = tmp_path / "test.db"
        db = AlertDatabase(str(db_path))
        assert os.path.exists(db_path)

    def test_save_and_retrieve_alert(self, tmp_path):
        """Test saving and retrieving alerts"""
        db_path = tmp_path / "test.db"
        db = AlertDatabase(str(db_path))

        alert = {
            "timestamp": "2024-01-01T00:00:00",
            "type": "motion",
            "message": "Test alert",
            "metadata": {"zone": "A"},
        }

        # Save alert
        alert_id = db.save_alert(alert)
        assert alert_id > 0

        # Retrieve alert
        alerts = db.get_alerts()
        assert len(alerts) == 1
        assert alerts[0]["type"] == "motion"
        assert alerts[0]["message"] == "Test alert"

    def test_get_alert_count(self, tmp_path):
        """Test getting alert count"""
        db_path = tmp_path / "test.db"
        db = AlertDatabase(str(db_path))

        # Add alerts
        db.save_alert(
            {
                "timestamp": "2024-01-01",
                "type": "motion",
                "message": "Test 1",
                "metadata": {},
            }
        )
        db.save_alert(
            {
                "timestamp": "2024-01-02",
                "type": "intrusion",
                "message": "Test 2",
                "metadata": {},
            }
        )

        # Check counts
        assert db.get_alert_count() == 2
        assert db.get_alert_count("motion") == 1
        assert db.get_alert_count("intrusion") == 1

    def test_filter_by_type(self, tmp_path):
        """Test filtering alerts by type"""
        db_path = tmp_path / "test.db"
        db = AlertDatabase(str(db_path))

        db.save_alert(
            {
                "timestamp": "2024-01-01",
                "type": "motion",
                "message": "Motion 1",
                "metadata": {},
            }
        )
        db.save_alert(
            {
                "timestamp": "2024-01-02",
                "type": "motion",
                "message": "Motion 2",
                "metadata": {},
            }
        )
        db.save_alert(
            {
                "timestamp": "2024-01-03",
                "type": "intrusion",
                "message": "Intrusion",
                "metadata": {},
            }
        )

        motion_alerts = db.get_alerts(alert_type="motion")
        assert len(motion_alerts) == 2

    def test_clear_alerts(self, tmp_path):
        """Test clearing alerts"""
        db_path = tmp_path / "test.db"
        db = AlertDatabase(str(db_path))

        db.save_alert(
            {
                "timestamp": "2024-01-01",
                "type": "motion",
                "message": "Test",
                "metadata": {},
            }
        )

        assert db.get_alert_count() == 1

        db.clear_alerts()
        assert db.get_alert_count() == 0
