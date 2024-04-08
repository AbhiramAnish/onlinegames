from django.urls import path
from . import views
urlpatterns = [
    path('',views.tiktak,name='tiktak'),
]