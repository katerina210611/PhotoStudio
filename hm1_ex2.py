def can_break_chocolate(length, width, piece_size):
  """
  Определяет, можно ли отломить кусок от шоколадки заданного размера.

  Args:
    length: Длина шоколадки.
    width: Ширина шоколадки.
    piece_size: Размер куска, который нужно отломить.

  Returns:
    True, если можно отломить кусок, False, если нельзя.
  """

  total_size = length * width

  if piece_size > total_size:
    return False  # Кусок больше, чем вся шоколадка

  if piece_size == 0:
    return False # Нельзя отломить кусок нулевого размера

  if piece_size % length == 0 or piece_size % width == 0:
    return True
  else:
    return False


# Примеры использования:
print(can_break_chocolate(3, 4, 6))   # True
print(can_break_chocolate(5, 7, 8))   # False
print(can_break_chocolate(4, 5, 12))  # True
print(can_break_chocolate(2, 10, 20)) # True
print(can_break_chocolate(2, 10, 19)) # False
print(can_break_chocolate(2, 10, 0))  # False # Дополнительный тест

