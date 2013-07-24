# import the User object
from django.contrib.auth.models import User

# Name my backend 'MyCustomBackend'
class MyCustomBackend:

    # Create an authentication method
    # This is called by the standard Django login procedure

    def authenticate(self, username=None, password=None):

        try:
            # Try to find a user matching your username
            my_user = User.objects.get(username=username)
            if my_user.user.check_password(password):
                return my_user.user
            else:
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None