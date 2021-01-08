class Roman_Numeral:
    def int_to_roman(self, num):
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1 ]
        roman_num = ''
        i = 0
        while  num > 0:
            # loop through
            for _ in range(num // values[i]):
                roman_num += symbol[i]
                num -= values[i]
            i += 1
        return roman_num

    def roman_to_int(self, roman):
        symbol = ["M", "D", "C", "L", "X", "V", "I"]
        values = [1000,500, 100,  50,  10,  5,   1 ]
        integer = 0
        for index_number in range(0, len(roman)):
            # print(roman[index_number])
            this_val = values[symbol.index(roman[index_number])]
            if roman[index_number] in symbol and index_number < len(roman)-1:
                next_val = values[symbol.index(roman[index_number+1])]
                if this_val < next_val:
                    integer -= this_val
                elif this_val == next_val or this_val > next_val:
                    integer += this_val
            else:
                integer += this_val
        return integer




print(Roman_Numeral().int_to_roman(44))
print(Roman_Numeral().roman_to_int("IV"))









