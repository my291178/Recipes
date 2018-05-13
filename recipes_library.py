
import json


def get_recipe_by_key(key, recipes):
    return recipes[key]["products"]


def get_recipes():
    with open("Recipes.json", "r") as f:
        return json.loads(f.read())