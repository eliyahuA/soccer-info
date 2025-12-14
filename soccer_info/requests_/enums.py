from enum import Enum


class ResponseFormat(str, Enum):
    """Supported response formats."""
    JSON = "json"
    CSV = "csv"
