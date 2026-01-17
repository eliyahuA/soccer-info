# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-01-17

### Added
- **Countries API domain support**:
  - `get_list()` - Retrieve country data including timezones, championship/player/team counts
  - Response models: `CountryListResponse`, `Country`

- **Matches API domain support** with 9 comprehensive methods:
  - **Single Match Endpoints**:
    - `get_view_basic()` - Fetch basic match details
    - `get_view_full()` - Fetch complete match details with lineups and events
    - `get_odds()` - Retrieve betting odds (1X2, handicaps, over/under) from multiple bookmakers
    - `get_progressive()` - Get progressive match data with timeline snapshots
  - **Day-Based Endpoints**:
    - `get_by_day_basic()` - Query basic match information by date
    - `get_by_day_full()` - Query complete match information by date
  - **Filter-Based Endpoints**:
    - `get_by_filter_basic()` - Filter matches by championship/manager/stadium (basic details)
    - `get_by_filter_full()` - Filter matches by championship/manager/stadium (complete details)
    - `get_by_filter_ids()` - Retrieve matches by specific match IDs

- **30+ new response models** for Matches domain organized by:
  - Match types: `MatchBasic`, `MatchFull`, `MatchOdds`, `MatchProgressive`
  - Match components: `Score`, `MatchStatistics`, `Lineup`, `MatchEvent`, `Timeline`
  - Odds data: `Bookmaker`, `OddsData`, `Bet365Odds`, `UnibetOdds`
  - Progressive data: `ProgressiveSnapshot`, `ProgressiveTimeline`
  - Response types: `MatchViewResponse`, `MatchOddsResponse`, `MatchProgressiveResponse`, `MatchListResponse`

- **Request parameter models** for all new endpoints:
  - `CountryListParameters`
  - `MatchViewParameters`, `MatchOddsParameters`, `MatchProgressiveParameters`
  - `MatchByDayParameters`, `MatchByFilterParameters`, `MatchByIdsParameters`

- **Example Jupyter notebook** (`season matches.ipynb`) demonstrating:
  - Fetching and filtering countries
  - Browsing championships
  - Retrieving Premier League matches from the last 2 weeks

### Changed
- Updated both synchronous and asynchronous clients with new domain modules
- Enhanced README documentation with Countries and Matches API sections

### Dependencies
- Added development dependencies for data exploration:
  - jupyterlab
  - pandas
  - ipython

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

[0.2.0]: https://github.com/eliyahuA/soccer-info/releases/tag/v0.2.0
[0.1.1]: https://github.com/eliyahuA/soccer-info/releases/tag/v0.1.1

