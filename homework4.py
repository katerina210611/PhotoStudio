def to_roman(number):
    """
    Преобразует целое положительное число в римское число.

    Args:
      number: Целое положительное число.

    Returns:
      Строка, представляющая римское число.  Возвращает None, если число не положительное.
    """

    if not isinstance(number, int) or number <= 0:
        return None  # Возвращаем None для некорректного ввода

    roman_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    roman_string = ''
    remaining = number

    for value, symbol in sorted(roman_map.items(), reverse=True):
        while remaining >= value:
            roman_string += symbol
            remaining -= value

    return roman_string


# Примеры использования:
print(to_roman(3))    # III
print(to_roman(15))   # XV
print(to_roman(234))  # CCXXXIV
print(to_roman(1))    # I
print(to_roman(4))    # IV
print(to_roman(9))    # IX
print(to_roman(44))   # XLIV
print(to_roman(3999)) # MMMCMXCIX
print(to_roman(0))    # None
print(to_roman(-5))   # None



