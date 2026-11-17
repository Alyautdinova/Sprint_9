from pages.base_page import BasePage
from locators.recipe_locators import RecipeLocators

class RecipePage(BasePage):
    
    # метод для получения текстового значения заголовка страницы рецепта
    def get_recipe_name_header(self):
        return self.get_text(RecipeLocators.recipe_name_header)