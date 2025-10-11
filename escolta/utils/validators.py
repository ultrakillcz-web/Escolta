"""
Validation utilities
"""

import re


def validate_sensor_id(sensor_id: str) -> bool:
    """
    Validate a sensor ID
    
    Args:
        sensor_id: Sensor ID to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not sensor_id or not isinstance(sensor_id, str):
        return False
    
    # Sensor ID should be alphanumeric with optional hyphens/underscores
    pattern = r'^[a-zA-Z0-9_-]+$'
    return bool(re.match(pattern, sensor_id))


def validate_severity(severity: str) -> bool:
    """
    Validate an alert severity level
    
    Args:
        severity: Severity level to validate
        
    Returns:
        True if valid, False otherwise
    """
    valid_severities = ["low", "medium", "high", "critical"]
    return severity.lower() in valid_severities


def validate_email(email: str) -> bool:
    """
    Validate an email address
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
