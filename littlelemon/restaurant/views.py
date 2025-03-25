from django.shortcuts import render
from rest_framework import generics
from .models import Menu , Booking
from .serializers import BookingSerializer, MenuItemSerializer
from rest_framework.viewsets import ModelViewSet
import datetime
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
def index(request):
    # On récupère l'année courante pour afficher-la dans la page HTML
    # On renvoie la page HTML avec la variable current_year remplie avec l'année courante

    return render(request, 'index.html', {
        'current_year' : datetime.date.today().year,
    })

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView (generics.RetrieveUpdateAPIView , generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]