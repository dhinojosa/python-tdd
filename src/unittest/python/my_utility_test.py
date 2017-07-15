import unittest

from hamcrest import *
from mockito import mock, verify

from my_utility import add


class MyUtilityTest(unittest.TestCase):
    @staticmethod
    def test_calculate_add():
        result = add(4, 2)
        assert_that(result, is_(equal_to(6)))
