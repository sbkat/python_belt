from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^wishes$', views.success),
    url(r'^wishes/new$', views.new_wish),
    url(r'^adding_a_wish$', views.adding_a_wish),
    url(r'^cancel$', views.cancel),
    url(r'^wishes/(?P<wish_id>\d+)/remove$', views.remove_wish),
    url(r'^wishes/edit/(?P<wish_id>\d+)$', views.edit_wish_page),
    url(r'^editing_wish/(?P<wish_id>\d+)$', views.editing_wish),
    url(r'^wishes/stats$', views.stats),
    url(r'^wishes/grant/(?P<wish_id>\d+)$', views.grant_wish),
    url(r'^wishes/like/(?P<wish_id>\d+)$', views.like_wish),
    url(r'^logout$', views.logout),
]