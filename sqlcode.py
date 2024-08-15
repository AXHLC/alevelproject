import os
from supabase import create_client, Client
from supabase.client import ClientOptions
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the supabase api key from .env
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set")

supabase = create_client(url, key,
  # Set timeout options
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
))