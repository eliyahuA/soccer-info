from typing import List, Optional
from pydantic import Field

from ..base import ResponseComponent, APIResponse


class Team(ResponseComponent):
    """Team reference in standings table."""
    id: str
    name: str


class TableEntry(ResponseComponent):
    """Single entry in a league standings table."""
    team: Team
    position: int
    win: int
    draw: int
    loss: int
    points: int
    goals_scored: int
    goals_conceded: int
    note: Optional[str] = None

    @property
    def matches_played(self) -> int:
        """Calculate total matches played."""
        return self.win + self.draw + self.loss

    @property
    def goal_difference(self) -> int:
        """Calculate goal difference."""
        return self.goals_scored - self.goals_conceded


class Group(ResponseComponent):
    """Group/league within a championship season."""
    name: str
    table: List[TableEntry]


class Season(ResponseComponent):
    """Championship season with date range and standings."""
    name: str
    from_date: str = Field(alias="from")
    to_date: str = Field(alias="to")
    groups: List[Group]


class ChampionshipListItem(ResponseComponent):
    """Championship item in list response."""
    id: str
    name: str
    has_image: bool


class ChampionshipDetail(ResponseComponent):
    """Detailed championship data with seasons."""
    id: str
    name: str
    country: str
    has_image: bool
    seasons: List[Season]


class ChampionshipListResponse(APIResponse[ChampionshipListItem]):
    """Response for championships list endpoint."""
    pass


class ChampionshipViewResponse(APIResponse[ChampionshipDetail]):
    """Response for championship view endpoint."""
    pass
