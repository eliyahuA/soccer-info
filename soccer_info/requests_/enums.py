from enum import Enum


class Language(str, Enum):
    """Supported language codes for API responses."""
    ENGLISH = "en_US"
    ITALIAN = "it_IT"
    SPANISH = "es_ES"
    FRENCH = "fr_FR"
    GERMAN = "de_DE"
    PORTUGUESE = "pt_PT"
    POLISH = "pl_PL"
    TURKISH = "tr_TR"
    RUSSIAN = "ru_RU"
    JAPANESE = "ja_JP"
    CHINESE = "zh_CN"
    ARABIC = "ar_SA"


class ResponseFormat(str, Enum):
    """Supported response formats."""
    JSON = "json"
    CSV = "csv"
