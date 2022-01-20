from django.urls import path
from lineups import views

urlpatterns = [

    path('', views.home, name='home'),
    path('bind', views.bind, name='bind')

]