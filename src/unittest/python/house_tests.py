import unittest

from hamcrest import *
from mockito import mock, unstub, verify
from house import House


# Test Double - Stub - Canned Answer
class KitchenStub:
    def __init__(self):
        self.temp = 0

    def set_oven(self, temp):
        self.temp = temp


class HouseTest(unittest.TestCase):
    """Think of the simplest thing first
       Therefore:
           The simplest test is an empty string and zero

    """

    # @staticmethod
    # def test_house_set_temp_to_350_using_stub():
    #     kitchen_stub = KitchenStub()  # collaborator
    #     house = House(kitchen_stub, None)  # subject under test
    #     house.bake_cookies()
    #     assert_that(kitchen_stub.temp, equal_to(350))

    @staticmethod
    def test_house_set_temp_to_350_using_mock():
        kitchen_mock = mock()
        house = House(kitchen_mock, None)  # subject under test
        house.bake_cookies()
        verify(kitchen_mock).set_oven(350)
        verify(kitchen_mock).set_oven(150)
        verify(kitchen_mock).set_oven(650)
        unstub()
