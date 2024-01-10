from rest_framework import serializers
from .models import Vehicle, Service, Petrol, Trip

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

    # def get_owner(self, obj):
    #     return{
    #         "id": obj.owner.id,
    #         "username": obj.owner.username,
    #         "number": obj.owner.profile.number,
    #         "address": obj.owner.profile.address,
    #     }

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PetrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petrol
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'