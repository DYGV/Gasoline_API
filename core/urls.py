from django.conf.urls import include, url
from django.contrib import admin
from APIs import views, apis
from APIs import serializers,views,models
from APIs.models import Gasoline, HighOctane, Diesel

urlpatterns = [
    url(r'^$', apis.guide, name='guide'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(apis.router.urls)),
]
