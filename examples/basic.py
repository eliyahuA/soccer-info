"""
Synchronous example using paginated championship API requests.

Demonstrates:
- Sync client with context manager (quick_client)
- Paginated API response handling
- Random sampling across pages
- Rate limit monitoring

Process:
1. Fetch championships list metadata
2. Randomly select 20 championship indices
3. Calculate page numbers and indices using divmod()
4. Group requests by page number
5. Fetch required pages and extract championships
6. Display timing and rate limit information
"""
import random
from datetime import datetime
from dotenv import load_dotenv
from soccer_info import quick_client
from textwrap import dedent
from collections import defaultdict
from soccer_info.responses import APIResponse, ChampionshipViewResponse

load_dotenv()


def print_status(response: APIResponse):
    """
    Print HTTP status and rate limit information from an API response.
    
    Args:
        response: Any APIResponse object containing response_headers
        
    Displays:
        - HTTP status code
        - Remaining rate limit quota and total limit
        - Time until rate limit reset (in hours and seconds)
    """
    headers = response.response_headers
    print(dedent(f"""             
             Result Status - {response.status}
             Rate Limit: {headers.rate_limit_remaining}/{headers.rate_limit_limit} remaining
             Reset in: {headers.hours_to_reset} hours ({headers.rate_limit_reset} seconds)                 
             """))


def print_championship_details(championship_detail: ChampionshipViewResponse):
    """
    Print detailed information about a championship including standings.
    
    Args:
        championship_detail: ChampionshipViewResponse containing full championship data
        
    Displays:
        - Country code
        - Number of seasons available
        - Most recent season name (if available)
        - Groups/leagues within the last season
        - Team standings table for each group
    """
    print("Championship details:")
    print(f"country: {championship_detail.first_result.country}")
    seasons = len(championship_detail.first_result.seasons)
    print(f"seasons: {seasons}", end='')
    if seasons > 0:
        last_season = championship_detail.first_result.seasons[-1]
        last_season_name = last_season.name
        print(f" last season: {last_season_name}")
        for group in last_season.groups:
            print(f"group: {group.name}")
            for row in group.table:
                print(f"\t{row.team.name}")

    else:
        print('')


def main():
    """
    Demonstrate paginated championship fetching with rate limit monitoring.

    1. Fetching initial metadata to get total championship count
    2. Randomly selecting 20 championship indices (0 to total_count-1)
    3. Calculate which page and index each championship is on
    4. Fetching the necessary pages
    5. Extracting the specific championships
    6. Print detailed data for each selected championship

    """
    start_time = datetime.now()

    with quick_client() as client:

        print("Getting championships dataset")
        response = client.championships.get_list()
        print_status(response)

        # Randomly select 20 championships from the total available
        total_championships = response.pagination[0].items
        random_championships = random.sample(range(total_championships), min(20, total_championships))

        # Group championships by page to minimize API requests
        # Key: page number, Value: list of indices on that page
        championships_to_get = defaultdict(list)
        for championship in random_championships:
            # Calculate page and index: divmod(24, 25) = (0, 24) → page 1, index 24
            page, index = divmod(championship, response.pagination[0].per_page)
            page += 1  # API pages are 1-based, not 0-based
            championships_to_get[page].append(index)

        # Fetch only the pages we need
        for page, championship_indexes in championships_to_get.items():
            print(f"Getting championships page {page}")
            championships = client.championships.get_list(page=page)
            print_status(championships)
            
            # Process all championships we need from this page
            for championship_index in championship_indexes:
                championship_id = championships.result[championship_index].id
                championship_name = championships.result[championship_index].name
                print(f"Getting details for championship {championship_name} (id: {championship_id})")
                
                # Fetch detailed championship data including seasons and standings
                championship_detail = client.championships.get_by_id(championship_id)
                print_status(championship_detail)
                print_championship_details(championship_detail)

            print("="*80)
    print(f"Total processing time: {datetime.now() - start_time}")  # 0:00:18.844822


if __name__ == "__main__":
    main()
