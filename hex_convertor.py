class HexConvertor:
    _HEX_DIVIDER = 16
    _HEX_ARRAY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self, number):
        self.number = number

    def convert_int_to_hex(self):
        str_hex_number = ''
        while self.number > 0:
            str_hex_number += str(self._HEX_ARRAY[(self.number % self._HEX_DIVIDER)])
            self.number //= self._HEX_DIVIDER
        str_hex_number = str_hex_number[::-1]
        return str_hex_number


if __name__ == '__main__':
    new_hex = HexConvertor(16)
    print(new_hex.convert_int_to_hex())
