from rest_framework import viewsets
from .serializer import InventorySerializer
from .models import Inventory


# Create your views here.

class InventoryView(viewsets.ModelViewSet):
    serializer_class =InventorySerializer
    queryset = Inventory.objects.all()