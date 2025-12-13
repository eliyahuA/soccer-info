"""Response models for Soccer Football Info API."""
from .base import ResponseComponent, APIResponse, Pagination
from .championships import (
    ChampionshipListItem,
    ChampionshipListResponse,
    ChampionshipDetail,
    ChampionshipViewResponse,
    Season,
    Group,
    TableEntry,
    Team,
)

__all__ = [
    'ResponseComponent',
    'APIResponse',
    'Pagination',
    'ChampionshipListItem',
    'ChampionshipListResponse',
    'ChampionshipDetail',
    'ChampionshipViewResponse',
    'Season',
    'Group',
    'TableEntry',
    'Team',
]
