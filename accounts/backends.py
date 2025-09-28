# Creating a custom authentication backend that authenticates using email instead of the default username
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            # Looking up a user by their email address
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            return None # Authentication has failed
        
        if user.check_password(password): # automatically checks the given password against the one in the db
            return user # Authentication successfull
        return None
    
    # Session retrieval
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
        
