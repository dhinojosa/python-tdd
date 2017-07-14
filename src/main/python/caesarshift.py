CAN_ONLY_BE_A_STRING_MSG = "Parameter can only be a string"
CAN_ONLY_BE_A_NUMBER_MSG = "Shift can only be a number"

SMALL_A = 97
SMALL_Z = 122


class CaesarShift:
    def __init__(self, shift):
        if not isinstance(shift, int):
            raise Exception(CAN_ONLY_BE_A_NUMBER_MSG)
        self.shift = shift

    def __encodeChar(self, string):
        return chr((ord(string[0]) + self.shift - SMALL_A) % 26 + SMALL_A)

    def decode_char(self, string, new_shift):
        return chr((ord(string[0]) + new_shift - SMALL_A) % 26 + SMALL_A)

    def encode(self, string):
        if not isinstance(string, str):
            raise Exception(CAN_ONLY_BE_A_STRING_MSG)
        if string == "":
            return ""
        result = ""
        for c in string:
            result += self.__encodeChar(c)
        return result

    def decode(self, string):
        if string == "":
            return ""
        c = self.decode_char(string, -self.shift)
        print "Foo" + c
        return c
