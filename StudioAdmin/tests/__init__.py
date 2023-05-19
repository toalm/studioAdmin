# © ALM Solutions AB.
# Written by Tobias Alm
import logging

# Third Party

# Local
logging.basicConfig(format='%(asctime)s [%(levelname)s]%(filename)s%(funcName)s(%(lineno)s)'
                           '->%(message)s')
log = logging.getLogger(__file__)
