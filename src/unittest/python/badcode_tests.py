import unittest

from hamcrest import *

from badcode import MyService

class MyServiceTest(unittest.TestCase):
    """Think of the simplest thing first
       Therefore:
           The simplest test is an empty string and zero

    """

    # Red Bar
    @staticmethod
    def test_my_service():
        my_service = MyService()
        result = my_service.method_support(lambda s: {"message" : "done deal!"})
        assert_that(result, "done deal!")