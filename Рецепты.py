'''
Что можно приготовить из имеющихся продуктов.
'''

import json


persons = int(input('Введите количество персон: '))


with open("Recipes.json","r") as f:
    recipes = json.loads(f.read())



with open("data.json","r") as f:
    fridge = json.loads(f.read())

result = []

for name, recipe in recipes.items():

    is_valid = True
    for i in recipe:
        if not fridge[i] >= recipe[i]*persons:
            is_valid = False
            break

    if is_valid:
        result.append(name)

print(result)
