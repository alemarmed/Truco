from rest_framework import serializers
from server_truco.models import Users

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    """Resource  mSeodel PointOfSale
    """
    class Meta:
        model = Users
        fields = ('name', 'address', 'email')