import allure

from pages.create_recipe_page import CreateRecipePage
from pages.recipe_page import RecipePage
from data.urls import Urls
from data.data_test import RECIPE_DATA

class TestCreateRecipe:

    @allure.title('Создание рецепта')
    @allure.description('Проверяем, что рецепт создается')
    def test_create_recipe(self, login_user, driver):
        
        with allure.step('Создание рецепта'):
            createRecipePage = CreateRecipePage(driver)
            createRecipePage.open(Urls.CREATE_RECIPES_URL)

            createRecipePage.create_recipe(recipe_name=RECIPE_DATA["name"],
                                           tag_name="Завтрак",
                                           ingredients=RECIPE_DATA["ingredients"],
                                           describe=RECIPE_DATA["description"],
                                           time=RECIPE_DATA["cooking_time"],
                                           image=RECIPE_DATA["image_path"])

        with allure.step('Проверка, что находимся на странице рецепта'):
            recipePage = RecipePage(driver)
            assert Urls.RECIPES_URL in recipePage.get_current_url()

        with allure.step('Проверка названия рецепта'):
            recipePage.get_recipe_name_header() == RECIPE_DATA["name"]
