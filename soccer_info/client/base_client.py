from dataclasses import dataclass
from typing import Optional, TypeVar

from soccer_info.responses.base import ResponseComponent
from soccer_info.settings import Settings

T = TypeVar('T', bound=ResponseComponent)


@dataclass
class BaseClient:
    """Base client containing common settings for all client types."""
    settings: Settings
    default_language: Optional[str] = None
