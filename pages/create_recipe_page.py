from pages.base_page import BasePage
from locators.create_recipe_locators import CreateRecipeLocators

class CreateRecipePage(BasePage):

    # метод заполнения поля "Название рецепта"
    def set_recipe_name(self, recipe_name):
        self.send_keys(CreateRecipeLocators.recipe_name_input, recipe_name)

    # метод выбора тега (Завтра/Обед/Ужин)
    def click_tag_name(self, tag_name):
        self.click(CreateRecipeLocators.tag_option(tag_name))

    # метод заполнения поля "Ингредиенты"
    def set_ingredient_name(self, ingredient_name):
        self.send_keys(CreateRecipeLocators.ingredient_input, ingredient_name)
        self.click(CreateRecipeLocators.ingredient_option(ingredient_name))

    # метод заполнения поля "Вес"
    def set_amount(self, amount):
        self.send_keys(CreateRecipeLocators.amount_input, amount)

    # метод нажатия на кнопку "Добавить ингредиент"
    def click_add_ingredient_button(self):
        self.click(CreateRecipeLocators.add_ingredient_button)

    # метод добавление ингредиента
    def add_ingredient(self, ingredient_name, amount):
        self.set_ingredient_name(ingredient_name)
        self.set_amount(amount)
        self.click_add_ingredient_button()

    # метод заполнения поля "Время приготовления"
    def set_time(self, time):
        self.send_keys(CreateRecipeLocators.time_input, time)

    # метод заполнения поля "Описание рецепта"
    def set_describe(self, describe):
        self.send_keys(CreateRecipeLocators.describe_textarea, describe)

    # метод загрузки фотографии
    def set_image(self, image):
        self.send_keys(CreateRecipeLocators.file_input, image)

    # метод нажатия на кнопку "Создать рецепт"
    def click_create_recipe_button(self):
        self.click(CreateRecipeLocators.create_recipe_button)

    # метод создания рецепта
    def create_recipe(self, recipe_name, tag_name, ingredient_name, amount, time, describe, image):
        self.set_recipe_name(recipe_name)
        self.click_tag_name(tag_name)
        self.add_ingredient(ingredient_name=ingredient_name, amount=amount)
        self.set_time(time)
        self.set_describe(describe)
        self.set_image(image)
        self.click_create_recipe_button()
    