from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem 
from .serializers import MenuItemSerializer
from rest_framework.viewsets import ModelViewSet
import datetime
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    

class SingleMenuItemView (generics.RetrieveUpdateAPIView , generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
