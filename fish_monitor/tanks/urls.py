from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tanks/$', views.TankList.as_view()),
    url(r'^tanks/(?P<tank_id>[0-9]+)/$', views.TankDetail.as_view()),
    url(r'^tanks/(?P<tank_id>[0-9]+)/change/$', views.TankWaterChange.as_view()),
    url(r'^tanks/(?P<tank_id>[0-9]+)/fish/$', views.FishList.as_view()),
    url(r'^tanks/(?P<tank_id>[0-9]+)/fish/(?P<fish_id>[0-9]+)/$', views.FishDetail.as_view()),
]
