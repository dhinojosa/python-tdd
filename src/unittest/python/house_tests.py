import unittest

from hamcrest import *

from house import House

#Test Double
class KitchenStub:
    def __init__(self):
       self.temp = 0

    def setOven(self, temp):
       self.temp = temp

class HouseTest(unittest.TestCase):
    """Think of the simplest thing first
       Therefore:
           The simplest test is an empty string and zero

    """

    @staticmethod
    def test_house_set_temp_to_350():
        kitchen_stub = KitchenStub()
        house = House(kitchen_stub, None)
        house.bake_cookies()
        assert_that(kitchen_stub.temp, equal_to(350))
