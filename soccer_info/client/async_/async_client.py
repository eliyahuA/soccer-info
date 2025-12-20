from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type

from soccer_info.requests_.parameters import BaseParameters
from soccer_info.requests_.headers import Header
from soccer_info.client.base_client import BaseClient, T


@dataclass
class AsyncClient(BaseClient, ABC):
    """Base async_ client for Soccer Football Info API.
    
    Provides common functionality and initialization for async_ specialized clients.
    Contains shared settings and default language preferences.
    
    Attributes:
        settings: API configuration including authentication credentials
        default_language: Preferred language for API responses (optional)
    """

    @abstractmethod
    async def do_request(
            self,
            endpoint: str,
            params: BaseParameters,
            headers: Header,
            response_model: Type[T],
    ) -> T:
        """Execute async_ HTTP request to API endpoint.
        
        Args:
            endpoint: API endpoint path (e.g., "/championships/list/")
            params: Request parameters to include in the API call
            headers: HTTP headers including RapidAPI authentication
            response_model: Pydantic model class for response validation
            
        Returns:
            Validated response object of the specified model type
        """
        ...
