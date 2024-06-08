from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.Infomation,name="first_app"),
]