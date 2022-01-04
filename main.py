def get_data(filename):
    dish = []
    dish_dict = {}
    buffer_dict = {}
    cook_book = {}
    keys = ('ingredient_name', 'quantity', 'measure')
    with open(filename, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            quantity = int(file.readline().strip())
            for ingr in range(quantity):
                d = file.readline().strip().split('|')
                dish_dict.update(dict(zip(keys, d)))
                buffer_dict = dish_dict.copy()
                dish.append(buffer_dict)
            cook_book[dish_name] = dish
            dish = []
            file.readline()

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_data('recipes.txt')
    ingr_dict = cook_book.copy()
    ingr_list = []
    cook_book_finished = {}
    for d in dishes:
        if d in cook_book.keys():
            for dish, ingredients in cook_book.items():
                if dish == d:
                    for ingr in ingredients:
                        if ingr['ingredient_name'] not in ingr_list:
                            ingr_list.append(ingr['ingredient_name'])
                            for k, v in ingr.items():
                                name = ingr['ingredient_name']
                                i = ingr.copy()
                                i['quantity'] = int(i['quantity'])
                                del i['ingredient_name']
                                cook_book_finished[name] = i
                        else:
                            for k, v in ingr.items():
                                name = ingr['ingredient_name']
                                i = ingr.copy()
                                i['quantity'] = int(i['quantity'])
                                del i['ingredient_name']
                                cook_book_finished[name]['quantity'] += i['quantity']
                                break
    for name, count in cook_book_finished.items():
        for param in count.keys():
            if param == 'quantity':
                count[param] *= person_count

    return cook_book_finished

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }


# print(get_data('recipes.txt'))

print(get_shop_list_by_dishes(['Запеченный картофель', 'Жареный картофель'], 2))
