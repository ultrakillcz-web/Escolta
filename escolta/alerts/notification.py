"""
Notification system for sending alerts
"""

import logging
from typing import Dict, Any


logger = logging.getLogger(__name__)


class Notification:
    """
    Handles sending notifications through various channels
    """
    
    def __init__(self):
        """Initialize the notification system"""
        self.channels = {
            "email": [],
            "sms": [],
            "push": []
        }
        logger.info("Notification system initialized")
    
    def add_recipient(self, channel: str, recipient: str):
        """
        Add a recipient to a notification channel
        
        Args:
            channel: Notification channel (email, sms, push)
            recipient: Recipient address/identifier
        """
        if channel in self.channels:
            if recipient not in self.channels[channel]:
                self.channels[channel].append(recipient)
                logger.info(f"Recipient {recipient} added to {channel} channel")
    
    def remove_recipient(self, channel: str, recipient: str):
        """
        Remove a recipient from a notification channel
        
        Args:
            channel: Notification channel
            recipient: Recipient address/identifier
        """
        if channel in self.channels and recipient in self.channels[channel]:
            self.channels[channel].remove(recipient)
            logger.info(f"Recipient {recipient} removed from {channel} channel")
    
    def send_notification(self, channel: str, message: str, 
                         alert_data: Dict[str, Any] = None) -> bool:
        """
        Send a notification through a specific channel
        
        Args:
            channel: Notification channel
            message: Notification message
            alert_data: Optional alert data to include
            
        Returns:
            True if notification was sent successfully
        """
        if channel not in self.channels:
            logger.error(f"Invalid notification channel: {channel}")
            return False
        
        if not self.channels[channel]:
            logger.warning(f"No recipients configured for {channel} channel")
            return False
        
        # In a real implementation, this would send actual notifications
        # For now, we just log the notification
        for recipient in self.channels[channel]:
            logger.info(f"[{channel.upper()}] Sending to {recipient}: {message}")
        
        return True
    
    def broadcast_alert(self, message: str, alert_data: Dict[str, Any] = None):
        """
        Broadcast an alert to all configured channels
        
        Args:
            message: Alert message
            alert_data: Optional alert data to include
        """
        for channel in self.channels:
            if self.channels[channel]:
                self.send_notification(channel, message, alert_data)
