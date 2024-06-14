from  .views import *
from django.urls import path


urlpatterns = [
    path('input/',User_input,name='User_input'),
    path('',home,name='home'),
]