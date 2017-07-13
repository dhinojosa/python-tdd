CAN_ONLY_BE_A_NUMBER_MSG = "Shift can only be a number"

SMALL_A = 97
SMALL_Z = 122


class CaesarShift:
    def __init__(self, shift):
        if not isinstance(shift, int):
            raise Exception(CAN_ONLY_BE_A_NUMBER_MSG)
        self.shift = shift

    def encode(self, string):
        if not isinstance(string, str):
            raise Exception("Parameter can only be a string")
        if string == "":
            return ""
        return chr((ord(string[0]) + self.shift - SMALL_A) % 26 + SMALL_A)
