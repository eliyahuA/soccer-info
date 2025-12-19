import json
from dotenv import load_dotenv
from soccer_info import quick_client

load_dotenv()

with quick_client() as client:
    r = client.championships.get_list()
    print(json.dumps(r.model_dump(), indent=2))
    
    # Display rate limit information
    print("\nRate Limit Info:")
    print(f"  Limit: {r.response_headers.x_ratelimit_request_limit}")
    print(f"  Remaining: {r.response_headers.x_ratelimit_request_remaining}")
    print(f"  Reset in: {r.response_headers.hours_to_reset} hours")