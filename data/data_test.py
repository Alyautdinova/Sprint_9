import os
import random

RECIPE_DATA = {
    "name": f"Арепа {random.randint(1, 10000)}",
    "description": "Этот рецепт создан автотестом",
    "cooking_time": "10",
    "ingredients": [
        {"name": "кукурузная мука", "amount": "200"},
        {"name": "вода", "amount": "100"},
        {"name": "соль", "amount": "5"},
        {"name": "сыр", "amount": "50"}
    ],
    "image_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "arepa.jpg")
}
