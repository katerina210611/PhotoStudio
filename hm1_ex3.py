def count_weekends_before_vacation(days_left):
  """
  Вычисляет количество выходных дней до отпуска, считая от понедельника.

  Args:
    days_left: Количество дней до отпуска.

  Returns:
    Количество выходных дней (суббота и воскресенье) до отпуска.
  """

  weekends = 0
  for day in range(1, days_left + 1):
    day_of_week = (day + 1) % 7 # Сегодня понедельник (индекс 0). +1 чтобы начать с понедельника как с первого дня.

    if day_of_week == 5 or day_of_week == 6: # Суббота (индекс 5) и воскресенье (индекс 6).
      weekends += 1

  return weekends


# Примеры использования:
print(count_weekends_before_vacation(4))   # 0
print(count_weekends_before_vacation(6))   # 1
print(count_weekends_before_vacation(14))  # 4
print(count_weekends_before_vacation(7))  # 2
print(count_weekends_before_vacation(8))  # 2
print(count_weekends_before_vacation(9))  # 2
print(count_weekends_before_vacation(10)) # 2
print(count_weekends_before_vacation(11)) # 2
print(count_weekends_before_vacation(12)) # 3
print(count_weekends_before_vacation(13)) # 3

