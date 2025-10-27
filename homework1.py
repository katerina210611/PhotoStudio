def reverse_middle_digits(number):
  """
  Зеркально отражает три центральные цифры пятизначного числа.

  Args:
    number: Пятизначное число (целое или строка).

  Returns:
    Строка, представляющая число с отраженными центральными цифрами,
    или None, если введенное число не является пятизначным.
  """

  number_str = str(number)  # Преобразуем в строку для удобства работы с цифрами

  if len(number_str) != 5:
    return None  # Если число не пятизначное, возвращаем None

  first_digit = number_str[0]
  middle_digits = number_str[1:4]  # Выделяем три центральные цифры
  last_digit = number_str[4]

  reversed_middle_digits = middle_digits[::-1]  # Разворачиваем центральные цифры

  result = first_digit + reversed_middle_digits + last_digit  # Собираем результат

  return result


# Пример использования:
number = input("Введите пятизначное число: ")

reversed_number = reverse_middle_digits(number)

if reversed_number:
  print("Число с отраженными центральными цифрами:", reversed_number)
else:
  print("Ошибка: Введено не пятизначное число.")


