from django.conf.urls import url, include
from fish_monitor.api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^tanks/$', views.TankList.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
]
