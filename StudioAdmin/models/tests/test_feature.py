# © ALM Solutions AB.
# Written by Tobias Alm
import logging

from django.db import IntegrityError
# Third Party
from django.test import TestCase

from StudioAdmin.models import Product, Feature, Parameter, Quota

# Local
logging.basicConfig(format='%(asctime)s [%(levelname)s]%(filename)s%(funcName)s(%(lineno)s)'
                           '->%(message)s')
log = logging.getLogger(__file__)

TEST_FEATURE = 'TEST_FEATURE'
TEST_PARENT_FEATURE = 'TEST_PARENT_FEATURE'
TEST_PARAMETER_TOGGLE = 'TEST_PARAMETER_TOGGLE'
TEST_PARAMETER_INT = 'TEST_PARAMETER_INT'
TEST_PRODUCT_BRONZE = 'TEST_PRODUCT_BRONZE'


class FeatureTest(TestCase):

    def setUp(self) -> None:
        self.test_product = Product.objects.create(name=TEST_PRODUCT_BRONZE)
        self.test_feature = Feature.objects.create(name=TEST_FEATURE)
        self.test_feature.products.add(self.test_product)
        self.test_feature.save()
        self.test_parameter_toggle = Parameter.objects.create(name=TEST_PARAMETER_TOGGLE,
                                                              feature=self.test_feature)

    def test_to_create_parameters_for_feature(self):
        parameter_one = Parameter.objects.create(name=TEST_PARAMETER_TOGGLE,
                                                 feature=self.test_feature)
        self.assertIsNotNone(parameter_one)

    def test_to_set_a_quota_for_a_parameter_and_ensure_it_is_unique(self):
        quota = Quota.objects.create(parameter=self.test_parameter_toggle,
                                     product=self.test_product,
                                     value=2300)
        self.assertIsNotNone(quota)
        with self.assertRaises(expected_exception=IntegrityError) as ctx:
            Quota.objects.create(parameter=self.test_parameter_toggle,
                                 product=self.test_product)

        self.assertIsNotNone(ctx.exception)

    def test_to_create_parent_child_feature_relationship(self):
        parent_feature = Feature.objects.create(name=TEST_PARENT_FEATURE)
        self.test_feature.parent = parent_feature
        self.test_feature.save()
        self.assertIsNotNone(self.test_feature)
