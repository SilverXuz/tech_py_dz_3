"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""


def main():
    d = friends_items()
    ai = all_items(d)
    print("\nСписок всех вещей всех друзей:\n", ai)
    ui = uniq_items(d)
    print("\nСписок уникальных вещей, которые есть только у одного друга:\n", ui)
    common_items, missing_friend = looser(d)
    print("\nВещи, которые есть у всех друзей кроме одного:\n", common_items)
    print("Имя друга, у которого данные вещи отсутствуют:", missing_friend)
    # Код не учитывает ситуации, при которых может оказаться больше чем 1 решение для looser()


def friends_items():
    """
    ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
    :return: dict
    """
    items = {
        'Друг1': ('Рюкзак', 'Палатка', 'Спальник', 'Фонарик'),
        'Друг2': ('Рюкзак', 'Палатка', 'Котелок', 'Кружка'),
        'Друг3': ('Рюкзак', 'Палатка', 'Спички', 'Кружка')
    }
    return items


def all_items(items):
    """
    ✔ Какие вещи взяли все три друга.
    :param items: dict
    :return: list
    """
    all_items = [item for sublist in items.values() for item in sublist]
    return all_items


def uniq_items(items):
    """
    ✔ Какие вещи уникальны, есть только у одного друга
    :param d: dict
    :return: list
    """
    unique_items = []
    for item in set(sum(items.values(), ())):
        count = sum(item in friend_items for friend_items in items.values())
        if count == 1:
            unique_items.append(item)
    return unique_items


def looser(items):
    """
    ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует.
    :param items: dict
    :return: common_items = list, missing_friend = string
    """
    friend_count = len(items)
    item_counts = {}

    # Считаем количество повторений каждого предмета
    for friend in items:
        for item in items[friend]:
            item_counts[item] = item_counts.get(item, 0) + 1

    common_items = [item for item, count in item_counts.items() if count == friend_count - 1]

    missing_friend = None

    # Ищем друга, у которого отсутствуют общие предметы
    for friend in items:
        if not any(item in items[friend] for item in common_items):
            missing_friend = friend
            break
    return common_items, missing_friend


if __name__ == '__main__':
    main()
