from rest_framework import serializers
from .models import restaurant,Menu,Food



class RestaurantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = restaurant
        fields = '__all__'
    

class MenuSerializer(serializers.ModelSerializer):
    hr_restoran = serializers.CharField(source='restoran.name',read_only=True)
    hr_created_by = serializers.CharField(source='created_by.username',read_only=True)
    class Meta:
        model = Menu
        fields = ['name','id','created_by','restoran','hr_restoran','hr_created_by']
    

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

