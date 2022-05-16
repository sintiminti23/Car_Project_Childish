from rest_framework import serializers
from .models import UserCar, CarBrand, CarModel


class CarBrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    created_at = serializers.DateField()
    deleted_at = serializers.DateField()

    def create(self, validated_data):
        return CarBrand.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created_at = validated_data.get(
            'created_at', instance.created_at)
        instance.deleted_at = validated_data.get(
            'deleted_at', instance.deleted_at)
        instance.save()
        return instance


class CarModelSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')

    class Meta:
        model = CarModel
        fields = ['car_brand', 'name', 'created_at', 'deleted_at']


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ['user', 'car_brand', 'car_model',
                  'first_reg', 'odometer', 'created_at', 'deleted_at']
