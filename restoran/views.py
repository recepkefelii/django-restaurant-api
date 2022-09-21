from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import restaurant,Menu,Food
from .serializer import RestaurantSerializer,MenuSerializer,FoodSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class RestoranAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request:Request):
        
        Restoranlar = restaurant.objects.filter(created_by=request.user)
        serializer = RestaurantSerializer(Restoranlar,many=True) 
        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
        

    def post(self,request:Request):
        data = request.data
        user_id = request.user.id
        data['created_by'] = user_id

        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class MenuanAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    serializer_class = MenuSerializer
    search_fields = ['name','restoran__name','created_by__username']
    filterset_fields = ['name', 'restoran']
    

   
