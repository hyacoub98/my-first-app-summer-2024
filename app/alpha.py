# ENV VARS

# this is the "app/alpha.py" file...

import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env variables

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")
