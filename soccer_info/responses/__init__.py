"""Response models for Soccer Football Info API."""
from .base import ResponseComponent, APIResponse, Pagination, ResponseHeaders
from .championships import (
    ChampionshipListItem,
    ChampionshipListResponse,
    ChampionshipDetail,
    ChampionshipViewResponse,
    ChampionshipSeasonResponse,
    Season,
    Group,
    TableEntry,
    Team,
)

__all__ = [
    'ResponseComponent',
    'APIResponse',
    'Pagination',
    'ResponseHeaders',
    'ChampionshipListItem',
    'ChampionshipListResponse',
    'ChampionshipDetail',
    'ChampionshipViewResponse',
    'ChampionshipSeasonResponse',
    'Season',
    'Group',
    'TableEntry',
    'Team',
]
