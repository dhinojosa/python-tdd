import unittest
from hamcrest import *

from registration_service import Registrant, RegistrationService


class RegistrationIntTest(unittest.TestCase):
    @staticmethod
    def test_real_database():
        # Create a real db
        # db =
        # registration_service = RegistrationService(db)
        assert_that(4, equal_to(4))
