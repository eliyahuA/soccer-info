from dataclasses import dataclass
from typing import Optional

from soccer_info.requests_ import ChampionshipListParameters, ChampionshipViewParameters, ChampionshipBySeasonParameters
from soccer_info.responses import ChampionshipListResponse, ChampionshipViewResponse, ChampionshipSeasonResponse
from ..async_client import AsyncClient
from ...common.domain.championships import Championships as CommonChampionships


@dataclass
class AsyncChampionships(CommonChampionships):
    """Asynchronous domain client for championship-related API endpoints."""

    client: AsyncClient

    async def get_list(
        self,
        page: Optional[int] = None,
        country: Optional[str] = None,
        language: Optional[str] = None,
    ) -> ChampionshipListResponse:
        return await self.client.do_request(
            endpoint="/championships/list/",
            params=ChampionshipListParameters(
                page=page,
                country=country,
                language=self._get_language(language),
            ),
            headers=self._header_provider(),
            response_model=ChampionshipListResponse,
        )

    async def get_by_id(
        self,
        championship_id: str,
        language: Optional[str] = None,
    ) -> ChampionshipViewResponse:
        return await self.client.do_request(
            endpoint="/championships/view/",
            params=ChampionshipViewParameters(
                id=championship_id,
                language=self._get_language(language),
            ),
            headers=self._header_provider(),
            response_model=ChampionshipViewResponse,
        )

    async def get_by_season(
        self,
        championship_id: str,
        season: str,
        language: Optional[str] = None,
    ) -> ChampionshipSeasonResponse:
        """Get standings for a specific championship season (async).
        
        Args:
            championship_id: ID of the championship
            season: Season year (e.g., "2023/2024")
            language: Language code
            
        Returns:
            Standings and details for the requested season
        """
        return await self.client.do_request(
            endpoint="/championships/season/",
            params=ChampionshipBySeasonParameters(
                id=championship_id,
                season=season,
                language=self._get_language(language),
            ),
            headers=self._header_provider(),
            response_model=ChampionshipSeasonResponse,
        )
