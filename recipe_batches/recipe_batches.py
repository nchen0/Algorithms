#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    foods_amt = []
    recipe_list = []
    ingredient_list = []
    for i, food in recipe.items():
        if i not in recipe_list:
            recipe_list.append(i)
        for j, ingredient in ingredients.items():
            if j not in ingredient_list:
                ingredient_list.append(j)
            if i == j:
                foods_amt.append(ingredient / food)
    if len(recipe_list) > len(ingredient_list):
        return 0
    else:
        return math.floor(min(foods_amt))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
