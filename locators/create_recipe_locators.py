from selenium.webdriver.common.by import By

class CreateRecipeLocators:
    recipe_name_input = [By.XPATH, "//div[text()='Название рецепта']/following-sibling::input"]
    ingredient_input = [By.XPATH, "//div[text()='Ингредиенты']/following-sibling::input"]
    amount_input = [By.XPATH, "//div[contains(@class,'ingredientsAmountInput')]//input"]
    add_ingredient_button = [By.XPATH, "//div[text()='Добавить ингредиент']"]
    time_input = [By.XPATH, "//div[text()='Время приготовления']/following-sibling::input"]
    describe_textarea = [By.XPATH, "//div[text()='Описание рецепта']/following-sibling::textarea"]
    file_input = [By.XPATH, "//input[@type='file']"]
    create_recipe_button = [By.XPATH, "//button[text()='Создать рецепт']"]

    # завтрак, обед или ужин
    @staticmethod
    def tag_option(tag_name):
        return (By.XPATH, f"//button/following-sibling::span[text()='{tag_name}']")

    @staticmethod
    def ingredient_option(ingredient_name):
        return (By.XPATH, f"//div[contains(@class,'styles_ingredientsInputs')]//div[contains(@class,'styles_container')]/div[text()='{ingredient_name}']")
    