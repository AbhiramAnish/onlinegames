from django.urls import path
from . import views
urlpatterns = [
    path('tiktak/',views.tiktak,name='tiktak'),
    path('',views.index,name='index'),
    path('stone/',views.stone,name='stone'),
    path('animal/',views.animal,name='animal'),



]