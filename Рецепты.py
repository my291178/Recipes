'''
Что можно приготовить из имеющихся продуктов.
'''

from recipes_library import *

print_data(get_result(get_json_from_file("Recipes.json"), get_json_from_file("data.json"), get_persons()))

#result.txt