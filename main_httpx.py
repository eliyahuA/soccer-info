import os
from httpx import Client
from dotenv import load_dotenv

load_dotenv()

client = Client()

r = client.get(
    url="https://soccer-football-info.p.rapidapi.com/matches/by/basic/",
    params={"c": "220fb8b4d337b6"},
    headers={
        "x-rapidapi-key": f"{os.getenv("x-rapidapi-key")}",
        "x-rapidapi-host": "soccer-football-info.p.rapidapi.com"
    },
)
print(r.text)


