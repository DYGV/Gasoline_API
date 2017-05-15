from rest_framework import viewsets, routers ,filters,serializers
from .models import Gasoline, HighOctane, Diesel
from .serializers import Serializer
from django.shortcuts import render
import datetime


def guide(request):
    date = {'date': datetime.datetime.today()}
    return render(request, 'index.html',  date)


class GasolineRank(viewsets.ModelViewSet):
    queryset = Gasoline.objects.all()
    serializer_class = Serializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('rank', 'pref', 'price', 'date')


class HighOctaneRank(viewsets.ModelViewSet):
    queryset = HighOctane.objects.all()
    serializer_class = Serializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('rank', 'pref', 'price', 'date')


class DieselRank(viewsets.ModelViewSet):
    queryset = Diesel.objects.all()
    serializer_class = Serializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('rank', 'pref', 'price', 'date')


router = routers.DefaultRouter()
router.register(r'gasoline', GasolineRank)
router.register(r'high-octane', HighOctaneRank)
router.register(r'diesel', DieselRank)

