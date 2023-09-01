import logging
from django.http import HttpResponse
from django.template import loader
from common.const import CONST_LOG_NAME

log = logging.getLogger(CONST_LOG_NAME)


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
