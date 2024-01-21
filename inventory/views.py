from rest_framework import viewsets
from .serializer import InventorySerializer, UsersSerializer
from .models import Inventory, Users


# Create your views here.

class InventoryView(viewsets.ModelViewSet):
    serializer_class =InventorySerializer
    queryset = Inventory.objects.all()
    
class UsersView(viewsets.ModelViewSet):
    serializer_class =UsersSerializer
    queryset = Users.objects.all()
    
    