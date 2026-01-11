# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2025-01-09

### Added
- Initial release of soccer-info SDK
- Championship API endpoints support:
  - `get_list()` - Browse and filter championships by country
  - `get_by_id()` - Get detailed championship data with seasons and standings
- Synchronous client (`HTTPXClient`) implementation
- Asynchronous client (`AsyncHTTPXClient`) with built-in rate limiting
- Flexible API key configuration:
  - Environment variable support
  - Direct key injection
  - Custom key provider functions
- Pydantic response models for type-safe data access:
  - `ChampionshipListResponse`
  - `ChampionshipViewResponse`
  - `ChampionshipListItem`
  - `ChampionshipDetail`
  - `Season`, `Group`, `TableEntry`, `Team`
- Response features:
  - Rate limit header parsing
  - JSON export with `save_pretty_json()`
  - Convenience properties (`first_result`, `is_success`)
- Context manager support for automatic resource cleanup
- Language parameter support for localized responses
- Quick client factory functions:
  - `quick_client()` for synchronous usage
  - `quick_async_client()` for asynchronous usage
- Type hints support with PEP 561 `py.typed` marker
- Comprehensive documentation and usage examples
- MIT License

### Dependencies
- httpx >= 0.25.0 for HTTP client functionality
- pydantic >= 2.0.0 for response validation and parsing

### Requirements
- Python 3.13 or higher
- RapidAPI account with Soccer Football Info API subscription

[0.1.1]: https://github.com/eliyahuA/soccer-info/releases/tag/v0.1.1

