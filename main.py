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


print(get_data('recipes.txt'))
