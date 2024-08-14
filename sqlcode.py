
import os
from supabase import create_client, Client
from supabase.client import ClientOptions

# get the supabase api key from .env
url: str = os.environ.get("SUPABASE_URL")

# get the supabase url from .env
key: str = os.environ.get("SUPABASE_KEY")


supabase: Client = create_client(url, key,

  # set timeout options
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
))


# SELECT name, dob, id FROM trackerdata  WHERE id = 5
