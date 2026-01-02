"""Request building components for Soccer Football Info API."""
from .headers import Header
from .parameters import (
    BaseParameters,
    ChampionshipListParameters,
    ChampionshipViewParameters,
    ChampionshipBySeasonParameters
)

__all__ = [
    'Header',
    'BaseParameters',
    'ChampionshipListParameters', 
    'ChampionshipViewParameters',
    'ChampionshipBySeasonParameters',
]
