def is_positive_float(data):
  """
  Проверяет, является ли строка положительным вещественным числом (без встроенных функций).

  Args:
    data: Строка, которую нужно проверить.

  Returns:
    True, если строка представляет положительное вещественное число, False в противном случае.
  """

  if not isinstance(data, str):
    return False  # Должна быть строка

  if not data:
    return False  # Пустая строка - не число

  dot_count = 0
  digit_seen = False  # Была ли хотя бы одна цифра?

  for i, char in enumerate(data):
    if char.isdigit():
      digit_seen = True  # Запомнили, что видели цифру
    elif char == '.':
      dot_count += 1
      if dot_count > 1:
        return False  # Больше одной точки - не число
      if i == 0 and len(data) == 1:
        return False # Если строка состоит только из точки "."
    else:
      return False  # Не цифра и не точка - не число

  if not digit_seen:
    return False # Если не было ни одной цифры

  # Проверка, что строка не состоит только из точки
  if data == ".":
      return False

  return True


def is_negative_float(data):
    """
    Проверяет, является ли строка отрицательным вещественным числом.
    """
    if data.startswith('-'):
        return is_positive_float(data[1:])  # Проверяем остальную часть как положительное

    return False


# Примеры использования:
print(is_positive_float("5.6"))   # True
print(is_positive_float(".78"))   # True
print(is_positive_float(".67."))  # False
print(is_positive_float("5"))     # True
print(is_positive_float("5."))    # True
print(is_positive_float("."))     # False
print(is_positive_float("abc"))   # False
print(is_positive_float(""))      # False
print(is_positive_float("5.6.7")) # False
print(is_positive_float("0.0"))   # True
print(is_positive_float("0"))     # True

print(is_negative_float("-5.6"))   # True
print(is_negative_float("-.78"))   # True
print(is_negative_float("-5"))     # True
print(is_negative_float("5.6"))    # False
print(is_negative_float("-.5.6"))    # False
