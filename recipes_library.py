
import json


class RecipesLibrary:

    def __init__(self, path_to_recipes, path_to_fridge):
        self._recipes = self._get_json_from_file(path_to_recipes)
        self._fridge = self._get_json_from_file(path_to_fridge)
        self._persons = self._get_persons()

    @staticmethod
    def _get_persons():
        return int(input('Введите количество персон: '))

    def _get_recipe_by_key(self, key):
        return self._recipes[key]["products"]

    def _print_data(self, data):
        with open("result.txt", "w") as f:
            for name in data:
                f.write(f"{name} {self._get_description_by_key(name)}")
                f.write("\n")

    @staticmethod
    def _get_json_from_file(filename):
        with open(filename, "r") as f:
            return json.loads(f.read())

    def _get_description_by_key(self, key):
        return self._recipes[key]["description"]

    def _get_result(self):
        result = []
        for name in self._recipes:

            is_valid = True
            recipe = self._get_recipe_by_key(name)

            for i in recipe:
                if not self._fridge[i] >= recipe[i] * self._persons:
                    is_valid = False
                    break

            if is_valid:
                result.append(name)

        return result

    def show_available_recipe(self):
        self._print_data(self._get_result())
