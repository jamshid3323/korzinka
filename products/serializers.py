from rest_framework import serializers
from .models import ProductModel, CategoryModel


class CategoryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductModelSerializers(serializers.ModelSerializer):
    # category = CategoryModelSerializers()

    class Meta:
        model = ProductModel
        fields = '__all__'
        # exclude = ['created_at']

    def create(self, validated_data):
        print('Create function ishladi')
        return ProductModel.objects.create(**validated_data)