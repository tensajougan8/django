from django.shortcuts import render
from rest_framework import viewsets, permissions
# from rest_framework.authtoken.admin import User
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny
from .models import Vehicle, Service, Petrol, Trip
from .serializers import VehicleSerializer, ServiceSerializer, PetrolSerializer, TripSerializer

# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PetrolViewSet(viewsets.ModelViewSet):
    queryset= Petrol.objects.all()
    serializer_class = PetrolSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return Response({"error": "Invalid username or password."}, status= status.HTTP_400_BAD_REQUEST)
#
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key})
#
# class RegisterView(APIView):
#     permission_classes = [AllowAny]
#     def get(self,request):
#         return Response({'get'})
#
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         number = request.data.get("number")
#         address = request.data.get("address")
#         if User.objects.filter(username=username).exists():
#             return Response({"error": "A user with that username already exists."}, status=status.HTTP_400_BAD_REQUEST)
#
#         user = User.objects.create_user(username=username, password = password)
#         profile = Profile.objects.create(user=user,number=number,address=address)
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key})

# Create your views here.
