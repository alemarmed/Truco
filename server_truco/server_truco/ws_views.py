from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from server_truco.resources import RegisterSerializer
from server_truco.models import Users

class RegisterView(APIView):
    """
    API endpoint that represents a list of users.
    """
    model = Users
    serializer_class = RegisterSerializer