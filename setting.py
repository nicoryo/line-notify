import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY     = os.environ.get("api_key")
API_SECRET  = os.environ.get("api_secret_key")
Line_API    = os.environ.get("line_key")