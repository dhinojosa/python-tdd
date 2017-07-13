import unittest

from hamcrest import *

from caesarshift import CaesarShift


class CaesarShiftTest(unittest.TestCase):
    """Think of the simplest thing first
       Therefore:
           The simplest test is an empty string and zero

    """

    # Red Bar
    @staticmethod
    def test_empty_string_with_shift_of_zero():
        caesar_shift = CaesarShift(0)
        result = caesar_shift.encode("")
        assert_that(result, equal_to(""))

    # Red Bar
    @staticmethod
    def test_letter_a_with_shift_of_zero():
        caesar_shift = CaesarShift(0)
        result = caesar_shift.encode("a")
        assert_that(result, equal_to("a"))

    # Red Bar
    @staticmethod
    def test_letter_a_with_shift_of_one():
        caesar_shift = CaesarShift(1)
        result = caesar_shift.encode("a")
        assert_that(result, equal_to("b"))

    # Red Bar
    @staticmethod
    def test_letter_z_with_shift_of_one():
        caesar_shift = CaesarShift(1)
        result = caesar_shift.encode("z")
        assert_that(result, equal_to("a"))

    # Red Bar
    @staticmethod
    def test_letter_z_with_shift_of_26_times_4():
        caesar_shift = CaesarShift(26 * 4)
        result = caesar_shift.encode("z")
        assert_that(result, equal_to("z"))

