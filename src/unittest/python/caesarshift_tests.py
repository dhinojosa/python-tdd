import unittest

from hamcrest import *

from caesarshift import CaesarShift, CAN_ONLY_BE_A_NUMBER_MSG, CAN_ONLY_BE_A_STRING_MSG


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

    # Green Bar
    @staticmethod
    def test_letter_z_with_shift_of_28():
        caesar_shift = CaesarShift(28)
        result = caesar_shift.encode("z")
        assert_that(result, equal_to("b"))

    # Red Bar
    def test_giving_a_string_for_a_shift(self):
        try:
            CaesarShift("WOW")
            self.fail("This should not pass")
        except Exception as e:
            assert_that(e.message, equal_to(CAN_ONLY_BE_A_NUMBER_MSG))

    # Red Bar
    def test_encode_with_different_type(self):
        try:
            caesar_shift = CaesarShift(1)
            caesar_shift.encode(49)
            self.fail("This should not pass")
        except Exception as e:
            assert_that(e.message, equal_to(CAN_ONLY_BE_A_STRING_MSG))

    # Red Bar
    @staticmethod
    def test_a_word_a_shift_of_one():
        caesar_shift = CaesarShift(1)
        result = caesar_shift.encode("hello")
        assert_that(result, equal_to("ifmmp"))

    # Red Bar
    @staticmethod
    def test_empty_string_decode_with_shift_of_zero():
        caesar_shift = CaesarShift(0)
        result = caesar_shift.decode("")
        assert_that(result, equal_to(""))

    # Red Bar
    @staticmethod
    def test_letter_a_decode_with_shift_of_zero():
        caesar_shift = CaesarShift(0)
        result = caesar_shift.decode("a")
        assert_that(result, equal_to("a"))

    # Red Bar
    @staticmethod
    def test_letter_a_decode_with_shift_of_one():
        caesar_shift = CaesarShift(1)
        result = caesar_shift.decode("f")
        assert_that(result, equal_to("e"))





    #Oh oh capital letters
    #Strange characters?
    #decode