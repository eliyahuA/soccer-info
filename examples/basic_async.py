"""
Asynchronous example using concurrent paginated championship API requests.

Demonstrates:
- Async client with context manager (quick_async_client)
- Paginated API response handling
- Random sampling across pages
- Concurrent page fetching with asyncio.gather()
- Concurrent championship detail fetching
- Rate limit monitoring

Process:
1. Fetch championships list metadata
2. Randomly select 20 championship indices
3. Calculate page numbers and indices using divmod()
4. Group requests by page number
5. Fetch required pages concurrently
6. Fetch championship details concurrently
7. Display timing and rate limit information
"""
import asyncio
import random
from collections import defaultdict
from datetime import datetime
from dotenv import load_dotenv
from soccer_info import quick_async_client
from examples.basic import print_status, print_championship_details

load_dotenv()


async def main():
    """
    Demonstrate concurrent paginated championship fetching with rate limit monitoring.

    1. Fetch initial metadata to get total championship count
    2. Randomly select 20 championship indices (0 to total_count-1)
    3. Calculate which page and index each championship is on
    4. Fetch necessary pages concurrently
    5. Extract specific championships
    6. Fetch championship details concurrently
    7. Display results with timing and rate limit information
    """
    start_time = datetime.now()

    async with quick_async_client() as client:
        print("Getting championships dataset")
        response = await client.championships.get_list()
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

        # Fetch all required pages concurrently
        print(f"Fetching {len(championships_to_get)} pages concurrently...")
        page_tasks = [
            client.championships.get_list(page=page)
            for page in championships_to_get.keys()
        ]
        page_results = await asyncio.gather(*page_tasks)

        # Build mapping of page -> response
        pages_data = dict(zip(championships_to_get.keys(), page_results))

        # Print status for each page fetch
        for page, page_response in pages_data.items():
            print(f"Page {page} fetched")
            print_status(page_response)

        # Collect all championship IDs to fetch
        print(f"Fetching {len(random_championships)} championship details concurrently...")
        detail_tasks = []
        for page, indices in championships_to_get.items():
            for idx in indices:
                champ_id = pages_data[page].result[idx].id
                champ_name = pages_data[page].result[idx].name
                print(f"Queuing championship: {champ_name} (id: {champ_id})")
                detail_tasks.append(client.championships.get_by_id(champ_id))

        # Fetch all championship details concurrently
        detail_results = await asyncio.gather(*detail_tasks)

        # Process and display results
        print("\n" + "="*80)
        print("Championship Details:")
        print("="*80 + "\n")
        for detail in detail_results:
            print_status(detail)
            print_championship_details(detail)
            print("-"*80)

    print(f"Total processing time: {datetime.now() - start_time}")

if __name__ == "__main__":
    asyncio.run(main(), debug=True)
