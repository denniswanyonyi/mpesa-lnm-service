import requests
import os

class Utilities:

    def set_access_token(self):
        
        try:

            URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

            # Get access token from os environment
            token_request = requests.get(URL, timeout=30, auth=(os.environ["C2B_CONSUMER_KEY"], os.environ["C2B_CONSUMER_SECRET"]))

            print("Utilities: ", token_request.json())

            if token_request.status_code == 200:
                os.environ["C2B_ACCESS_TOKEN"] = token_request.json()["access_token"]
        
        except TimeoutError as timeoutError:
            print(timeoutError)
            # TO DO: log exception

        except ConnectionError as connectionError:
            print(connectionError)
            # TO DO: log exception

