"""
✔ Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
from collections import Counter

new_list = [1, 2, 2, 8, 3, 1, 0, 2, 0, "1", "1", "2"]
print(f"Исходный список: \n", new_list)

counter = Counter(new_list)
double_list = [item for item, count in counter.items() if count > 1]
print("\nСписок с дублирующимися элементами: \n", double_list)

result_list = list(set(new_list))
print(f"\nКонечный список: \n", result_list)
