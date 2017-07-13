

class CaesarShift:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, string):
        # get the first char
        # shift if by self.shift
        # return result
        # https://github.com/dhinojosa/python-tdd
        if string == "":
            return ""
        elif string:
            return chr(ord(string[0]) + self.shift)
