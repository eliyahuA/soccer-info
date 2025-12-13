import httpx
from typing import Optional, Type, TypeVar

from soccer_info.requests_ import enums
from soccer_info.requests_.headers import Header
from soccer_info.requests_.parameters import BaseParameters
from soccer_info.responses.base import ResponseComponent
from soccer_info.settings import Settings
from .base_client import BaseClient
from .championships import Championships

T = TypeVar('T', bound=ResponseComponent)


class Client(BaseClient):
    """Main client for Soccer Football Info API interactions.
    
    Provides high-level access to all API endpoints through specialized
    domain clients (championships, teams, players, etc.). Handles request 
    execution with httpx, response parsing, and error handling.
    
    Example:
        >>> from soccer_info import quick_client
        >>> client = quick_client()
        >>> championships = client.championships.get_list()
        >>> for champ in championships.result:
        ...     print(f"{champ.name} (ID: {champ.id})")
    """

    def __init__(
            self,
            settings: Settings,
            default_language: Optional[enums.Language] = None,
            timeout: float = 30.0,
    ):
        """Initialize the main Soccer API client.
        
        Args:
            settings: API configuration including authentication credentials
            default_language: Preferred language for API responses (optional)
            timeout: Request timeout in seconds (default: 30.0)
        """
        super().__init__(settings, default_language)
        self._timeout = timeout
        self._http_client: Optional[httpx.Client] = None
        
        # Initialize domain clients
        self.championships = Championships(self, self._do_request)

    @property
    def http_client(self) -> httpx.Client:
        """Lazily initialize and return the httpx client."""
        if self._http_client is None:
            self._http_client = httpx.Client(
                base_url=self.settings.base_url,
                timeout=self._timeout,
            )
        return self._http_client

    def _do_request(
            self,
            endpoint: str,
            params: BaseParameters,
            headers: Header,
            response_model: Type[T],
    ) -> T:
        """Execute HTTP request to Soccer Football Info API endpoint.
        
        Args:
            endpoint: API endpoint path (e.g., "/championships/list/")
            params: Request parameters to include in the API call
            headers: HTTP headers including RapidAPI authentication
            response_model: Pydantic model class for response validation
            
        Returns:
            Validated response object of the specified model type
            
        Raises:
            httpx.HTTPStatusError: If the request fails with non-2xx status
            RuntimeError: If the response indicates an API error
        """
        response = self.http_client.get(
            endpoint,
            params=params.to_dict(),
            headers=headers.to_dict(),
        )
        
        response.raise_for_status()
        
        return response_model.model_validate_json(response.text)

    def close(self) -> None:
        """Close the HTTP client and release resources."""
        if self._http_client is not None:
            self._http_client.close()
            self._http_client = None

    def __enter__(self) -> 'Client':
        """Enter context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager and close client."""
        self.close()
