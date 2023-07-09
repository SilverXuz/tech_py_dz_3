"""
✔ Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
"""

def main():
    items = {
        'Рюкзак': 50, 'Палатка': 100, 'Спальник': 20, 'Фонарик': 5, 'Складной стул': 15, 'Спички': 1
    }
    max_weight = 160
    backpack, total_weight = fit_items_in_backpack(items, max_weight)
    print("Вещи, которые влезут в рюкзак:")
    for item in backpack:
        print(item)
    print(f"Загруз {total_weight}/{max_weight}")


def fit_items_in_backpack(items, max_weight):
    backpack = []
    total_weight = 0

    # Сортируем вещи по массе в невозрастающем порядке
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)

    for item, weight in sorted_items:
        # Если вещь помещается в рюкзак, добавляем ее и обновляем общую массу
        if total_weight + weight <= max_weight:
            backpack.append(item)
            total_weight += weight

    return backpack, total_weight

if __name__ == '__main__':
    main()
