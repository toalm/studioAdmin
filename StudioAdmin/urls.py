# © ALM Solutions AB.
# Written by Tobias Alm
import logging

# Third Party
from django.urls import path

from StudioAdmin import views

# Local
logging.basicConfig(format='%(asctime)s [%(levelname)s]%(filename)s%(funcName)s(%(lineno)s)'
                           '->%(message)s')
log = logging.getLogger(__file__)

app_name = "StudioAdmin"
urlpatterns = [
    path('', views.index, name='index'),
]
