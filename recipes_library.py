
import json


def get_persons():
    return int(input('Введите количество персон: '))


def get_recipe_by_key(key, recipes):
    return recipes[key]["products"]


def print_data(result):
    with open("result.txt", "w") as f:
        for name in result:
            f.write(name + "\n")


def get_json_from_file(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())


def get_description_by_key(resipes, key):
    return resipes[key]["description"]


def get_result(recipes, fridge, persons):
    result = []
    for name in recipes:

        is_valid = True
        recipe = get_recipe_by_key(name, recipes)

        for i in recipe:
            if not fridge[i] >= recipe[i] * persons:
                is_valid = False
                break

        if is_valid:
            result.append(name)

    return result

