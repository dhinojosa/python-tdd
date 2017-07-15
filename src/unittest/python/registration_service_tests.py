import unittest

from hamcrest import *
from mockito import mock, unstub, when, verify
from registration_service import Registrant, RegistrationService


class RegistrationServiceTest(unittest.TestCase):
    # My bet:
    # Use when, when you need to return something, or raise something
    # if nothing is being returned, use verify

    @staticmethod
    def test_insert_registrant_susan_harper():
        # Setting up the mocks
        db_mock = mock()  # mock
        cursor_mock = mock()  # mock

        # Rehearsing
        when(db_mock).cursor().thenReturn(cursor_mock)

        registration_service = RegistrationService(db_mock)
        registrant = Registrant("Susan", "Harper", 40, "New Jersey")  # dummy
        registration_service.insert(registrant)

        verify(cursor_mock, 1).execute("INSERT INTO REGISTRANT VALUES "
                                       "(\'Susan\', \'Harper\', 40, \'New Jersey\')")
        verify(db_mock).commit()
        verify(db_mock).close()
        unstub(db_mock, cursor_mock)

    @staticmethod
    def test_insert_registrant_carol_benjamin():
        # Setting up the mocks
        db_mock = mock()  # mock
        cursor_mock = mock()  # mock

        # Rehearsing
        when(db_mock).cursor().thenReturn(cursor_mock)

        registration_service = RegistrationService(db_mock)
        registrant = Registrant("Carol", "Benjamin", 22, "New York")  # dummy
        registration_service.insert(registrant)

        verify(cursor_mock, 1).execute("INSERT INTO REGISTRANT VALUES "
                                       "(\'Carol\', \'Benjamin\', 22, \'New York\')")
        verify(db_mock).commit()
        verify(db_mock).close()
        unstub(db_mock, cursor_mock)

    @staticmethod
    def test_insert_registrant_carol_benjamin():
        # Setting up the mocks
        db_mock = mock()  # mock
        cursor_mock = mock()  # mock

        # Rehearsing
        when(db_mock).cursor().thenReturn(cursor_mock)

        when(cursor_mock).execute("INSERT INTO REGISTRANT VALUES "
                                  "(\'Carol\', \'Benjamin\', 22, \'New York\')") \
            .thenRaise(Exception("Unable to connect to database"))

        registration_service = RegistrationService(db_mock)
        registrant = Registrant("Carol", "Benjamin", 22, "New York")  # dummy
        registration_service.insert(registrant)

        verify(db_mock).rollback()
        verify(db_mock).close()
        unstub(db_mock, cursor_mock)

    def test_insert_registrant_carol_benjamin_cursor_exception(self):
        # Setting up the mocks
        db_mock = mock()  # mock

        # Rehearsing
        when(db_mock).cursor().thenRaise(Exception("Unable to connect get cursor"))

        registration_service = RegistrationService(db_mock)
        registrant = Registrant("Carol", "Benjamin", 22, "New York")  # dummy

        try:
            registration_service.insert(registrant)
            self.fail("Should not be here")
        except Exception as e:
            assert_that(e.message, equal_to("Unable to get cursor"))

        verify(db_mock).close()
        unstub(db_mock)
