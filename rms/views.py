from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
#from rest_framework import generics
#from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework import filters
from .filters import FoodFilter
from django_filters import rest_framework as filter

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#from rest_framework.mixins
# Create your views here.
#@api_view(['GET','POST'])
#def category_list(request):
#class category_list(APIView):
#class category_list(generics.GenericAPIView):
#class category(ListAPIView,CreateAPIView): 
#class category(ListCreateAPIView):  
    #queryset = Category.objects
    #serializer_class = CategorySerializer
    #if request.method == "GET":
    #def get(self,request):
        #category = Category.objects.all()
        #category = self.queryset.all()
        #serializer = CategorySerializer(category,many=True)
        #return Response(serializer.data)
    #elif request.method == "POST":
    #def post(self,request):
        #serializer = CategorySerializer(data = request.data)
        #serializer.is_valid(raise_exception=True)
        ##serializer.save()
        #return Response({"detail:new Category created"},status=status.HTTP_201_CREATED)
    
#@api_view(['GET','DELETE','PUT'])
#class category_detail(APIView):
#class category_detail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#class category_detail(RetrieveUpdateDestroyAPIView):    
    #queryset = Category.objects.all()
    #serializer_class = CategorySerializer
    #lookup_field = 'id'
#def category_detail(request,id):
    #def get(self,request,id):
    #if request.method == "GET":
        #try:
            #category = Category.objects.get(id = id)
            #serializer = CategorySerializer(category)
            #return Response(serializer.data) 
        #except:
            #return Response({"detail category not found"},status=status.HTTP_404_NOT_FOUND) 
    #elif request.method == "DELETE":
    #def put(self,request,id):
        #category = Category.objects.get(id = id)
        #orderitem = OrderItem.objects.filter(food__category = category).count()
        #if orderitem > 0:
            #return Response({"details: this category exists in the order.Can not delete the category."})
        #category.delete()
        #return Response({"detail:Category deleted"}, status=status.HTTP_204_NO_CONTENT)
    #elif request.method == "PUT":
        #category = Category.objects.get(id = id)
        #serializer=CategorySerializer(category,data =request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #return Response(
            #{
                #"detail: Category updated"
                #"data":serializer.data
                #},status=status.HTTP_200_OK)
          
    
    def delete(self, request, id):
        category = Category.objects.get(id = id)
        orderitem = OrderItem.objects.filter(food__category = category).count()
        if orderitem > 0:
            return Response({"details: this category exists in the order.Can not delete the category."})
        category.delete()
        return Response({"detail:Category deleted"}, status=status.HTTP_204_NO_CONTENT)
              
class Foodviewset(ModelViewSet):
    queryset = Food.objects.select_related('category').all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    filterset_class = FoodFilter
    #filterset_fields = ['name']
    search_fields = ['name', 'description']
    