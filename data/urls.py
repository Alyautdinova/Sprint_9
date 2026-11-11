class Urls:
    BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru/"
    REGISTRATION_URL = BASE_URL + "signup"
    LOGIN_URL = BASE_URL + "signin"
    RECIPES_URL = BASE_URL + "recipes"
    CREATE_RECIPES_URL = RECIPES_URL + "/create"

    BASE_API = "https://foodgram-backend-1.foodgram.education-services.ru"
    API_LOGIN_URL = BASE_API + "/api/auth/token/login/"
    API_USERS = BASE_API + "/api/users/"
