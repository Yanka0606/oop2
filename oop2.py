cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def my_cook_book():
  with open('cook.txt', encoding='utf-8') as file:
    cook_book = {}
    #   # Нужно написать функцию, которая на входе берет список блюд из кулинарной книги и количество персон для кого мы будем готовить и возвращает список с названиями ингредиентов и колич

    for line in file:
      dish = line.strip()
      ingredients_count = int(file.readline())
      ingredients = []
      for i in range(ingredients_count):
        ingredient = file.readline().strip()
        ingredients.append(ingredient)
      cook_book[dish] = ingredients
      file.readline()


def get_shop_list_by_dishes(dishes, person_count):
  cook_book = my_cook_book()
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      new_shop_list_item = dict(ingredient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingredient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list


def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))


