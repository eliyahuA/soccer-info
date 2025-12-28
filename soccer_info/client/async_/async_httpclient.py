import asyncio
import httpx
import time
from typing import Optional, Type

from soccer_info.requests_.headers import Header
from soccer_info.requests_.parameters import BaseParameters
from soccer_info.responses.base import ResponseHeaders
from soccer_info.settings import Settings
from soccer_info.client.async_.async_client import AsyncClient, T
from soccer_info.client.async_.domain.championships import AsyncChampionships


class AsyncHTTPClient(AsyncClient):
    """Async client for Soccer Football Info API interactions.
    
    Provides high-level async_ access to all API endpoints through specialized
    domain clients (championships, teams, players, etc.). Handles async_ request
    execution with httpx, response parsing, and error handling.
    
    Example:
        >>> from soccer_info import quick_async_client
        >>> import asyncio
        >>> async def f():
        ...     async with quick_async_client() as client:
        ...     championships = await client.championships.get_list()
        ...     for champ in championships.result:
        ...         print(f'{champ.name} (ID: {champ.id})')
        >>> asyncio.run(f())
    """

    def __init__(
            self,
            settings: Settings,
            default_language: Optional[str] = None,
            timeout: float = 30.0,
    ):
        """Initialize the async_ Soccer API client.
        
        Args:
            settings: API configuration including authentication credentials
            default_language: Preferred language for API responses (optional)
            timeout: Request timeout in seconds (default: 30.0)
        """
        # Initialize base client (dataclass)
        super().__init__(settings, default_language)
        
        # Initialize HTTP client attributes
        self.timeout = timeout
        self._async_http_client: Optional[httpx.AsyncClient] = None
        
        # Initialize throttling mechanism
        self._throttle_lock = asyncio.Lock()
        self._last_request_time: Optional[float] = None
        
        # Initialize domain clients
        self.championships = AsyncChampionships(self)

    @property
    def async_http_client(self) -> httpx.AsyncClient:
        """Lazily initialize and return the httpx async_ client.
        
        The client is created on first access and reused for subsequent requests.
        """
        if self._async_http_client is None:
            self._async_http_client = httpx.AsyncClient(
                base_url=self.settings.base_url,
                timeout=self.timeout,
            )
        return self._async_http_client

    async def close(self) -> None:
        """Close the HTTP client and release resources."""
        if self._async_http_client is not None:
            await self._async_http_client.aclose()
            self._async_http_client = None

    async def __aenter__(self) -> 'AsyncHTTPClient':
        """Enter async_ context manager."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit async_ context manager and close client."""
        await self.close()

    async def do_request(
            self,
            endpoint: str,
            params: BaseParameters,
            headers: Header,
            response_model: Type[T],
    ) -> T:
        """Implements request throttling to ensure minimum time between requests.
        
        Requests are throttled according to settings.request_throttle_seconds. 
        If requests come in faster than the throttle limit, they will be queued 
        and processed sequentially with the appropriate delay.
        
        Raises:
            httpx.HTTPStatusError: If the request fails with non-2xx status
            RuntimeError: If the response indicates an API error
        """
        # Acquire lock to ensure proper spacing between request sends
        async with self._throttle_lock:
            # Calculate time to wait based on throttle setting
            if self._last_request_time is not None:
                elapsed = time.time() - self._last_request_time
                wait_time = self.settings.request_throttle_seconds - elapsed
                
                if wait_time > 0:
                    # Wait to respect the throttle limit
                    await asyncio.sleep(wait_time)
            
            # Update last request time before sending
            self._last_request_time = time.time()
        
        # Execute the HTTP request outside the lock so responses can overlap
        response = await self.async_http_client.get(
            endpoint,
            params=params.to_dict(),
            headers=headers.to_dict(),
        )

        response.raise_for_status()

        # Parse JSON response
        parsed = response_model.model_validate_json(response.text)

        # Parse and attach response headers (Pydantic handles normalization and type conversion)
        parsed.response_headers = ResponseHeaders.model_validate(dict(response.headers))

        return parsed
