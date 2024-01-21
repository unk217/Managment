from rest_framework import serializers
from .models import Inventory, Users


class InventorySerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField(source='age_r')
    
    
    
    class Meta:
        model = Inventory
        
        fields = '__all__'
        
class UsersSerializer(serializers.ModelSerializer):
     class Meta:
        model = Users
        fields = '__all__'        
        