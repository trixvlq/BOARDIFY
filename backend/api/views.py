from decouple import config
from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from Products.models import *
from Users.models import User
from .serializers import UserSerializer, ProductSerializer, CategorySerializer

import jwt, datetime


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        if request.COOKIES.get('jwt'):
            return UserView(request)

        user = User.objects.get(username=username)

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, config('SECRET_KEY'), algorithm=config('ALG'))

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'message': 'success',
            'jwt': token
        }

        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, config('SECRET_KEY'))
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.get(id=payload['id'])

        serializer = UserSerializer(user)

        return Response(serializer.data)


class ProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIView(generics.RetrieveAPIView):
    queryset = ProductSerializer
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        id = self.kwargs.get('id')
        return generics.get_object_or_404(queryset, id=id)


class CategoriesAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductSearchAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        queryset = Product.objects.filter(title__icontains=search_query)
        return queryset


class ProductTownSearchAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        town = self.request.query_params.get('town', '')
        queryset = Product.objects.filter(town=town)
        return queryset


class ProductCategorySearchAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', '')
        queryset = Product.objects.filter(category=category)
        return queryset
