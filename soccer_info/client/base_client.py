from typing import Optional

from soccer_info.settings import Settings


class BaseClient:
    """Base client for Soccer Football Info API.
    
    Provides common functionality and initialization for specialized clients.
    Contains shared settings and default language preferences.
    """

    def __init__(
            self,
            settings: Settings,
            default_language: Optional[str] = None,
    ):
        """Initialize the base client.
        
        Args:
            settings: API configuration including authentication credentials
            default_language: Preferred language for API responses (optional)
        """
        self.settings = settings
        self.default_language = default_language
