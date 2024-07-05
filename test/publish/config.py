import os
from dotenv import load_dotenv

# APPSYNC_ENDPOINT = "https://qyte2xsv3veorcshyitwogoyue.appsync-api.ap-northeast-1.amazonaws.com/graphql"
# APPSYNC_API_KEY = None

load_dotenv()


class Config:
    # appsync
    APPSYNC_API_URL = os.getenv('APPSYNC_API_URL', '')
    APPSYNC_API_KEY = os.getenv('APPSYNC_API_KEY')
