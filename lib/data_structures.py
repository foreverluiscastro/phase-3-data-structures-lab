
from functools import reduce
import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

def get_names(spicy_foods):
    pass
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    pass
    return [item for item in spicy_foods if item["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        # ipdb.set_trace()
        print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶" * food["heat_level"])
    
# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    cuisine_list = [food["cuisine"] for food in spicy_foods]
    cuisine_index = cuisine_list.index(cuisine)
    return spicy_foods[cuisine_index]
    # ipdb.set_trace()

get_spicy_food_by_cuisine(spicy_foods, "American")
    

def sort_by_heat(spicy_foods):
    pass
    sorted_list = sorted(spicy_foods, key=lambda food: food['heat_level'] )
    # ipdb.set_trace()
    return sorted_list
    
sort_by_heat(spicy_foods)

def print_spiciest_foods(spicy_foods):
    pass
    spice_over_five = [item for item in spicy_foods if item["heat_level"] > 5]
    for food in spice_over_five:
        # ipdb.set_trace()
        print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶" * food["heat_level"] )
        

print_spiciest_foods(spicy_foods)

def sum(a,b):
    return a + b

def get_average_heat_level(spicy_foods):
    pass
    all_spice = [item["heat_level"] for item in spicy_foods]
    total = reduce(sum, all_spice)
    return total / len(all_spice)
    # ipdb.set_trace()
        

get_average_heat_level(spicy_foods)