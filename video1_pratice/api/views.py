from django.shortcuts import render
from django.http import JsonResponse
from api.serializers import ProductSerializers
from api.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serilizer = ProductSerializers(products, many = True)

        return Response(serilizer.data, status=status.HTTP_200_OK)
