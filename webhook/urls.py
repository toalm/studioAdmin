# © ALM Solutions AB.
# Written by Tobias Alm
import logging

# Third Party
from django.urls import path

from common.const import CONST_LOG_NAME
from . import views

log = logging.getLogger(CONST_LOG_NAME)

app_name = "webhook"
urlpatterns = [
    path('stripe', views.stripe_webhook, name='webhook'),
]
