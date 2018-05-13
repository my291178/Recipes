'''
Что можно приготовить из имеющихся продуктов.
'''

from recipes_library import *


persons = int(input('Введите количество персон: '))


recipes = get_recipes()


with open("data.json","r") as f:
    fridge = json.loads(f.read())

result = []

for name in recipes:

    is_valid = True
    recipe = get_recipe_by_key(name, recipes)

    for i in recipe:
        if not fridge[i] >= recipe[i]*persons:
            is_valid = False
            break

    if is_valid:
        result.append(name)

print(result)





