"""
Event handling and processing for security events
"""

import logging
from typing import Dict, Any, Callable, List
from datetime import datetime


logger = logging.getLogger(__name__)


class EventHandler:
    """
    Handles and processes security events
    """
    
    def __init__(self):
        """Initialize the event handler"""
        self.event_callbacks = {}
        self.event_history = []
        logger.info("EventHandler initialized")
    
    def register_callback(self, event_type: str, callback: Callable):
        """
        Register a callback function for a specific event type
        
        Args:
            event_type: Type of event to handle
            callback: Callback function to execute when event occurs
        """
        if event_type not in self.event_callbacks:
            self.event_callbacks[event_type] = []
        self.event_callbacks[event_type].append(callback)
        logger.info(f"Callback registered for event type: {event_type}")
    
    def handle_event(self, event: Dict[str, Any]):
        """
        Process a security event and execute registered callbacks
        
        Args:
            event: Event dictionary containing event information
        """
        event_type = event.get("type", "unknown")
        event["processed_at"] = datetime.now().isoformat()
        
        self.event_history.append(event)
        
        if event_type in self.event_callbacks:
            for callback in self.event_callbacks[event_type]:
                try:
                    callback(event)
                except Exception as e:
                    logger.error(f"Error executing callback for {event_type}: {e}")
        
        logger.info(f"Event handled: {event_type}")
    
    def get_event_history(self, event_type: str = None, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Get event history, optionally filtered by type
        
        Args:
            event_type: Optional event type filter
            limit: Maximum number of events to return
            
        Returns:
            List of event dictionaries
        """
        if event_type:
            filtered = [e for e in self.event_history if e.get("type") == event_type]
            return filtered[-limit:]
        return self.event_history[-limit:]
