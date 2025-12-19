import asyncio
from dotenv import load_dotenv
from soccer_info import quick_async_client

load_dotenv()


async def f():

    async with quick_async_client() as client:
        championships = await client.championships.get_list()
        for champ in championships.result[0:10]:
            print(f"{champ.name} (ID: {champ.id})")

asyncio.run(f())
