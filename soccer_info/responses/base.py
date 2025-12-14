from pathlib import Path
from pydantic import BaseModel, ConfigDict
from typing import TypeVar, List, Generic, Any, Optional


class ResponseComponent(BaseModel):
    """Base model for Soccer Football Info API response parsing.
    
    Provides consistent validation and serialization behavior 
    for all API response models.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        extra='ignore'  # API may return additional fields
    )

    def save_pretty_json(self, target_file_path: Path) -> None:
        """Save the response to a JSON file with pretty formatting."""
        with open(target_file_path, 'w', encoding='utf-8') as f:
            f.write(self.model_dump_json(indent=4))


class Pagination(ResponseComponent):
    """Pagination information from API response."""
    page: int
    per_page: int
    items: int


T = TypeVar('T', bound=ResponseComponent)


class APIResponse(ResponseComponent, Generic[T]):
    """Standard API response wrapper.
    
    All Soccer Football Info API responses follow this structure with
    status, errors, pagination, and result fields.
    """
    status: int
    errors: List[str]
    pagination: List[Pagination]
    result: List[T]

    @property
    def is_success(self) -> bool:
        """Check if the response indicates success."""
        return self.status == 200 and len(self.errors) == 0

    @property
    def first_result(self) -> Optional[T]:
        """Get the first result item if available."""
        return self.result[0] if self.result else None

    @property
    def pagination_info(self) -> Optional[Pagination]:
        """Get pagination info if available."""
        return self.pagination[0] if self.pagination else None


class ForgivingResponse(ResponseComponent):
    """Unvalidated response model for development and debugging.
    
    Bypasses Pydantic validation to handle unknown or changing API structures.
    Should be avoided in production code - use typed response models instead.
    """
    model_config = ConfigDict(
        extra='allow',
        arbitrary_types_allowed=True
    )
