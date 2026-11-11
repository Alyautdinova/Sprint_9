# Sprint_9

## UI-тесты

Проект содержит автоматизированные UI-тесты для сервиса [Продуктовый помощник](https://foodgram-frontend-1.foodgram.education-services.ru/). Тесты написаны на Python с использованием Selenium WebDriver, Pytest и Allure.

## 🛠 Стек технологий

*   **Python 3.x**
*   **Selenium WebDriver** — для взаимодействия с браузером.
*   **Pytest** — фреймворк для написания тестов.
*   **Requests** — для подготовки тестовых данных через API (создание пользователей, заказов).
*   **Faker** — для генерации уникальных тестовых данных.
*   **Allure** — для генерации наглядных отчетов.

### Что проверяется

- **Создание пользователя**
- **Логин пользователя**
- **Создание рецепта**

### Запуск тестов с Allure

```bash
# 1. Запустить тесты с сохранением результатов
pytest --alluredir=target/allure-results --clean-alluredir

# 2. Сгенерировать HTML-отчёт
allure generate target/allure-results -o target/allure-report --clean

# 3. Открыть отчёт локально
allure open target/allure-report
```
