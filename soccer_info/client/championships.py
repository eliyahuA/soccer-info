from dataclasses import dataclass
from typing import Optional

from soccer_info.requests_.headers import Header
from soccer_info.requests_.parameters import (
    ChampionshipListParameters,
    ChampionshipViewParameters,
)
from soccer_info.responses.championships import (
    ChampionshipListResponse,
    ChampionshipViewResponse,
)
from .base_client import BaseClient


@dataclass
class Championships:
    """Domain client for championship-related API endpoints.
    
    Provides methods to retrieve championship information including
    lists, detailed views with seasons, groups, and standings.
    
    Attributes:
        client: Base client containing settings and do_request implementation
    """
    client: BaseClient
    
    def __post_init__(self):
        """Initialize the default header provider after dataclass initialization."""
        self._header_provider = lambda: Header(
            x_rapidapi_key=self.client.settings.api_key,
            x_rapidapi_host=self.client.settings.api_host,
        )

    def get_list(
            self,
            page: Optional[int] = None,
            country: Optional[str] = None,
            language: Optional[str] = None,
    ) -> ChampionshipListResponse:
        """Retrieve list of all championships.
        
        This is a paginated endpoint. Use the page parameter to navigate
        through results.
        
        Args:
            page: Page number for pagination (default: 1)
            country: Country code to filter championships (e.g., "IT", "ES")
            language: Language code for response (default: en_US)
            
        Returns:
            ChampionshipListResponse containing list of championships with pagination
        """
        return self.client.do_request(
            endpoint="/championships/list/",
            params=ChampionshipListParameters(
                page=page,
                country=country,
                language=language or self.client.default_language,
            ),
            headers=self._header_provider(),
            response_model=ChampionshipListResponse,
        )

    def get_by_id(
            self,
            championship_id: int,
            language: Optional[str] = None,
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
        return self.client.do_request(
            endpoint="/championships/view/",
            params=ChampionshipViewParameters(
                id=championship_id,
                language=language or self.client.default_language,
            ),
            headers=self._header_provider(),
            response_model=ChampionshipViewResponse,
        )
