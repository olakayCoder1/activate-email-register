from django.urls import path
from . import views



urlpatterns = [ 
    path('', views.register),
    path('activate-account/<uidb64>/<token>', views.activate_account, name="activate")
]