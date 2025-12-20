import asyncio
from dotenv import load_dotenv
from soccer_info import quick_async_client
from textwrap import dedent
load_dotenv()


async def f():

    async with quick_async_client() as client:
        championships = await client.championships.get_list()

        tasks = [
            asyncio.create_task(client.championships.get_by_id(champ.id))
            for champ in championships.result[0:1]
        ]

        for coro in asyncio.as_completed(tasks):
            response = await coro
            headers = response.response_headers
            
            print(dedent(f"""
            Result Status - {response.status}
            Rate Limit: {headers.rate_limit_remaining}/{headers.rate_limit_limit} remaining
            Reset in: {headers.hours_to_reset} hours ({headers.rate_limit_reset} seconds)
            Championship: {response.first_result.name} (ID: {response.first_result.id})            
            """))

if __name__ == "__main__":
    asyncio.run(f())
