from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import UserCar, CarBrand, CarModel
from .serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer


@csrf_exempt
def car_brand_list(request):
    if request.method == 'GET':
        car_brands = CarBrand.objects.all()
        serializer = CarBrandSerializer(car_brands, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarBrandSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def car_model_list(request):
    if request.method == 'GET':
        car_models = CarModel.objects.all()
        serializer = CarModelSerializer(car_models, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_car_list(request):
    if request.method == 'GET':
        user_cars = UserCar.objects.all()
        serializer = UserCarSerializer(user_cars, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserCarSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
