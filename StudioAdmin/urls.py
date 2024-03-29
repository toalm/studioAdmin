# © ALM Solutions AB.
# Written by Tobias Alm
import logging

# Third Party
from django.urls import path

from StudioAdmin import views

from common.const import CONST_LOG_NAME

log = logging.getLogger(CONST_LOG_NAME)


app_name = "StudioAdmin"
urlpatterns = [
    path('', views.index, name='index'),
]
