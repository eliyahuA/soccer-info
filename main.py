from dotenv import load_dotenv
from soccer_info import quick_client

load_dotenv()

client = quick_client()
r = client.championships.get_list()
print(r)
r.pagination_info
r.pagination[0].page
