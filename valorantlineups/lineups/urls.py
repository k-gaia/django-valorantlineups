from django.urls import path
from lineups import views

urlpatterns = [

    path('', views.home, name='home'),
    path('bind', views.bind, name='bind'),
    path('haven', views.haven, name='haven'),
    path('lineups_list', views.lineups_list, name='lineups_list'),
    path('child_lineups_list', views.child_lineups_list, name = 'child_lineups_list'),
    path('lineup_creator', views.lineup_creator, name = 'lineup_creator')

]