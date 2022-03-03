def intToRoman(num: int) -> str:
    specials = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    units = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ''
    i = 0
    while i < len(units) and num > 0:
        if units[i] > num:
            i += 1
        else:
            roman += specials[units[i]]
            num -= units[i]

    return roman


print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(9))
print(intToRoman(58))
print(intToRoman(1994))