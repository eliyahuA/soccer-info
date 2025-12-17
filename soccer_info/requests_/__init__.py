"""Request building components for Soccer Football Info API."""
from .headers import Header
from .parameters import BaseParameters, ChampionshipListParameters, ChampionshipViewParameters

__all__ = [
    'Header',
    'BaseParameters',
    'ChampionshipListParameters', 
    'ChampionshipViewParameters',
]
