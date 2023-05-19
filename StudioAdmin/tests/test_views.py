# © ALM Solutions AB.
# Written by Tobias Alm
import logging

# Third Party
from django.test import TestCase
# Local
logging.basicConfig(format='%(asctime)s [%(levelname)s]%(filename)s%(funcName)s(%(lineno)s)'
                           '->%(message)s')
log = logging.getLogger(__file__)


# Create your tests here.

class ViewTest(TestCase):

    def test_simple_view(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
