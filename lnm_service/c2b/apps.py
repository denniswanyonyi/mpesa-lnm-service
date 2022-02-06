from django.apps import AppConfig
from threading import Timer

from .utilities import Utilities

class C2BConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'c2b'


    # Adding code to initialize the access token that will be used if a user wants 
    # to perform a Lipa Na Mpesa (Pay Bill) transaction
    def ready(self):
        
        # This function sets the access token as an environment variable 
        # on django application start
        utilities = Utilities()
        utilities.set_access_token()

        # Run the function every 15 minutes to update the access token
        # timer = Timer(5, utilities.set_access_token)
        # timer.start()