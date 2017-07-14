CAN_ONLY_BE_A_STRING_MSG = "Parameter can only be a string"
CAN_ONLY_BE_A_NUMBER_MSG = "Shift can only be a number"

SMALL_A = 97
BIG_A = 65


class CaesarShift:
    def __init__(self, shift):
        if not isinstance(shift, int):
            raise Exception(CAN_ONLY_BE_A_NUMBER_MSG)
        self.shift = shift

    @staticmethod
    def __shift_char(char, new_shift):
        if not char.isalpha():
            return char
        a = BIG_A if char.isupper() else SMALL_A
        return chr((ord(char) + new_shift - a) % 26 + a)

    def __iterate_string(self, string, new_shift):
        if not isinstance(string, str):
            raise Exception(CAN_ONLY_BE_A_STRING_MSG)
        if string == "":
            return ""
        result = ""
        for c in string:
            result += self.__shift_char(c, new_shift)
        return result

    def encode(self, string):
        return self.__iterate_string(string, self.shift)

    def decode(self, string):
        return self.__iterate_string(string, -self.shift)
