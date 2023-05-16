# © ALM Solutions AB.
# Written by Tobias Alm
import logging

# Third Party
from django.db import models
from django.db.models import Model

# Local
logging.basicConfig(format='%(asctime)s [%(levelname)s]%(filename)s%(funcName)s(%(lineno)s)'
                           '->%(message)s')
log = logging.getLogger(__file__)


class Product(Model):
    name = models.CharField(db_column='COL_NAME',
                            max_length=128)

    class Meta:
        db_table = 'T_PRODUCT'


class Feature(Model):
    parent = models.ForeignKey(db_column='COL_PARENT',
                               to="self",
                               on_delete=models.CASCADE,
                               default=None,
                               null=True)
    name = models.CharField(db_column='COL_NAME',
                            max_length=128,
                            default='')
    products = models.ManyToManyField(to=Product,
                                      db_column="COL_PRODUCT_ID",
                                      related_name='features')

    class Meta:
        db_table = 'T_FEATURE'


class Quota(Model):
    product = models.ForeignKey(to=Product,
                                on_delete=models.CASCADE,
                                default=None)
    parameter = models.ForeignKey(to='Parameter',
                                  on_delete=models.CASCADE,
                                  default=None)

    value = models.IntegerField(db_column='COL_VALUE',
                                default=0)

    class Meta:
        db_table = 'T_QUOTA'
        unique_together = ['product', 'parameter']


class Parameter(Model):
    PARAM_TYPE_INT = 'int'
    PARAM_TYPE_STR = 'str'
    PARAM_TYPE_BOOL = 'bool'
    parameter_types = [
        (PARAM_TYPE_INT, 'Number'),
        (PARAM_TYPE_STR, 'Text'),
        (PARAM_TYPE_BOOL, 'Toggle')
        ]
    name = models.CharField(db_column='COL_NAME',
                            max_length=128,
                            default='')
    type = models.CharField(db_column='COL_TYPE',
                            choices=parameter_types,
                            default=PARAM_TYPE_BOOL,
                            max_length=16)
    feature = models.ForeignKey(to=Feature,
                                on_delete=models.CASCADE,
                                default=None)

    def __str__(self):
        return f'{self.name}->{self.type}'

    class Meta:
        db_table = 'T_PARAMETER'
