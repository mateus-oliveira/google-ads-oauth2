import os

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


_VERSION = "v10"


def create_client(refresh_token):
    try:
        credentials = {
            "developer_token": os.environ["DEVELOPER_TOKEN"],
            "client_id": os.environ["CLIENT_ID"],
            "client_secret": os.environ["CLIENT_SECRET"],
            "refresh_token": refresh_token,
            "use_proto_plus": "true"
        }
        return GoogleAdsClient.load_from_storage(credentials, version=_VERSION)
    except:
        raise ValueError("Invalid Refresh token")


def handle_errors():
    pass