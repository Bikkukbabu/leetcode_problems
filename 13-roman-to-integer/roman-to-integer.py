class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        number = 0
        previous_value = ''
        for char in s:
            if previous_value and (pv:=previous_value+char) in roman_map.keys():
                number = number - roman_map[previous_value]
                number = number+roman_map[pv]
            else:
                number = number+roman_map[char]
            previous_value = char
        return number