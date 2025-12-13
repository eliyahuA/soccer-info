from typing import Optional, Callable, Type, TypeVar

from soccer_info.requests_ import enums
from soccer_info.requests_.headers import Header
from soccer_info.requests_.parameters import (
    BaseParameters,
    ChampionshipListParameters,
    ChampionshipViewParameters,
)
from soccer_info.responses.base import ResponseComponent
from soccer_info.responses.championships import (
    ChampionshipListResponse,
    ChampionshipViewResponse,
)
from .base_client import BaseClient

T = TypeVar('T', bound=ResponseComponent)


class Championships:
    """Domain client for championship-related API endpoints.
    
    Provides methods to retrieve championship information including
    lists, detailed views with seasons, groups, and standings.
    """

    def __init__(
            self,
            client: BaseClient,
            request_callable: Callable[..., T],
    ):
        """Initialize the Championships client.
        
        Args:
            client: Base client containing settings and configuration
            request_callable: Function to execute API requests
        """
        self._client = client
        self._request_callable = request_callable
        self._default_header_provider = lambda: Header(
            x_rapidapi_key=self._client.settings.api_key,
            x_rapidapi_host=self._client.settings.api_host,
        )

    def get_list(
            self,
            page: Optional[int] = None,
            country: Optional[str] = None,
            language: Optional[enums.Language] = None,
            format_: Optional[enums.ResponseFormat] = None,
    ) -> ChampionshipListResponse:
        """Retrieve list of all championships.
        
        This is a paginated endpoint. Use the page parameter to navigate
        through results.
        
        Args:
            page: Page number for pagination (default: 1)
            country: Country code to filter championships (e.g., "IT", "ES")
            language: Language code for response (default: en_US)
            format_: Response format - json or csv (default: json)
            
        Returns:
            ChampionshipListResponse containing list of championships with pagination
        """
        return self._request_callable(
            endpoint="/championships/list/",
            params=ChampionshipListParameters(
                page=page,
                country=country,
                language=language or self._client.default_language,
                format=format_,
            ),
            headers=self._default_header_provider(),
            response_model=ChampionshipListResponse,
        )

    def get_by_id(
            self,
            championship_id: int,
            language: Optional[enums.Language] = None,
    ) -> ChampionshipViewResponse:
        """Retrieve detailed championship data including seasons and standings.
        
        Returns championship details with all seasons, groups within seasons,
        and full standings tables.
        
        Args:
            championship_id: The unique identifier of the championship
            language: Language code for response (default: en_US)
            
        Returns:
            ChampionshipViewResponse containing detailed championship data
        """
        return self._request_callable(
            endpoint="/championships/view/",
            params=ChampionshipViewParameters(
                id=championship_id,
                language=language or self._client.default_language,
            ),
            headers=self._default_header_provider(),
            response_model=ChampionshipViewResponse,
        )
