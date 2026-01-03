from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Optional


class BaseParameters(BaseModel):
    """Base model for Soccer Football Info API request parameters.
    
    Provides parameter validation and serialization for API requests.
    Uses short parameter names as per API specification.
    """
    
    model_config = ConfigDict(
        populate_by_name=True,
    )

    @model_validator(mode='before')
    @classmethod
    def remove_none_values(cls, data):
        """Remove None values from input data before model validation."""
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data

    def to_dict(self) -> dict:
        """Serialize model to dictionary for API requests.
        
        Returns:
            Dictionary with parameter names suitable for API requests
        """
        return self.model_dump(by_alias=True, exclude_none=True, mode='json')


class ChampionshipListParameters(BaseParameters):
    """Parameters for championships list endpoint.
    
    Attributes:
        page: Page number for pagination (default: 1)
        country: Country code filter (default: "all")
        language: Language code for response (default: en_US)
    """
    page: Optional[int] = Field(default=None, alias="p")
    country: Optional[str] = Field(default=None, alias="c")
    language: Optional[str] = Field(default=None, alias="l")


class ChampionshipViewParameters(BaseParameters):
    """Parameters for championship view endpoint.
    
    Attributes:
        id: Championship ID (required)
        language: Language code for response (default: en_US)
    """
    id: str = Field(alias="i")
    language: Optional[str] = Field(default=None, alias="l")


class ChampionshipBySeasonParameters(BaseParameters):
    """Parameters for championship by season endpoint.
    
    Attributes:
        id: Championship ID (required)
        season: Season year (required)
        language: Language code for response (default: en_US)
    """
    id: str = Field(alias="i")
    season: str = Field(alias="s")
    language: Optional[str] = Field(default=None, alias="l")
