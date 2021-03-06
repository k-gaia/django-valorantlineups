from atexit import register
from django.urls import path
from lineups import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.home, name='home'),
    path('bind', views.bind, name='bind'),
    path('haven', views.haven, name='haven'),
    path('split', views.split, name='split'),
    path('ascent', views.ascent, name='ascent'),
    path('lineups_list', views.lineups_list, name='lineups_list'),
    path('child_lineups_list', views.child_lineups_list, name = 'child_lineups_list'),
    path('agents_list', views.agents_list, name='agents_list'),
    path('lineup_creator', views.lineup_creator, name = 'lineup_creator'),
    path('latest_child_id', views.get_latest_childlineup_id, name='get_latest_childlineup_id'),
    path('pin_creator', views.pin_creator, name = 'pin_creator'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)