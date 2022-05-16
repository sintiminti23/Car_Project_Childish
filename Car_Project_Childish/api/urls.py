from django.urls import path
from Car_Project_Childish.api.view import car_brand_list, car_model_list, user_car_list


urlpatterns = [
    path('car_brand', car_brand_list),
    path('car_models', car_model_list),
    path('user_cars', user_car_list),
]
