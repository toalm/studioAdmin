# -*- coding: utf-8  -*-
# © Great Minds AB.
# Written by Tobias Alm
# System
import logging

# Third Party
from django.urls import path

from common.const import CONST_LOG_NAME
# Local
from .views import sign_up

log = logging.getLogger(CONST_LOG_NAME)


app_name = 'accounts'

urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    ]
