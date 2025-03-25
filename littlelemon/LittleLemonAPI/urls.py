from django.urls import path , include
from . import views
from rest_framework import routers


urlpatterns = [

    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),

]

