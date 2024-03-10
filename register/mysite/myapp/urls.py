from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup')
]

htmx_urlpatterns =[
    path('check_username/',views.check_username,name='check-username')
]

urlpatterns += htmx_urlpatterns