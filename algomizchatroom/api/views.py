from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from chat.models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/product',
        'GET/product/:id',

    ]
    return Response(routes)
 
@api_view(['GET'])
def getProducts(request):
    rooms = Product.objects.all()
    serializer = ProductSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    room = Product.objects.get(id=pk)
    serializer = ProductSerializer(room, many=False)
    return Response(serializer.data)



