from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.
class ListView(APIView):
    def get(self, request:Request, pk=None):
        if pk:
            try:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product)
                return Response(ProductSerializer(product).data)
            except:
                return Response({"error": "Product not found"})
            
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)
    
    def post(self, request:Request, pk=None):
        if not pk:    
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            products = serializer.save()
            return Response(ProductSerializer(products).data)
        return Response({'message':'Method POST not allowed'})

    def put(self, request:Request, pk=None):
        if pk:
            try:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer(instance=product, data=request.data)
                serializer.is_valid(raise_exception=True)
                product = serializer.save()
                return Response(ProductSerializer(product).data)
            except:
                return Response({"error": "Product not found"})
        return Response({'message':'Method PUT not allowed'})

    def delete(self, request:Request, pk=None):
        if pk:
            try:
                product = Product.objects.get(pk=pk)
                product.delete()
                return Response({"message": "Product deleted successfully"})
            except:
                return Response({"error": "Product not found"})
        return Response({'message':'Method DELETE not allowed'})