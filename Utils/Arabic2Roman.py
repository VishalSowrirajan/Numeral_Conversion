def arabic2roman(arabic_number):
    roman_number_map = numeral_mapping()
    roman_numeral = ''
    if arabic_number == 0:
        return 'nulla'
    else:
        while arabic_number > 0:
            for arab_no, rom_no in roman_number_map:
                while arabic_number >= arab_no:
                    roman_numeral += rom_no
                    arabic_number -= arab_no
        return roman_numeral


def roman2arabic(num):
    roman_numerals = roman_dict()
    result = 0
    if num == 'nulla':
        return result
    else:
        for i, c in enumerate(num):
            if (i+1) == len(num) or roman_numerals[c] >= roman_numerals[num[i+1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return result


def roman_dict():
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return roman_numerals


def numeral_mapping():
    roman_number_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                        (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    return roman_number_map
