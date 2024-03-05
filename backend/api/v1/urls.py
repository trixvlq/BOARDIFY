from django.urls import path, include

from ..views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('product/', ProductAPIView.as_view(), name='product'),
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('product-search/', ProductSearchAPIView.as_view(), name='search'),
    path('product-townsearch/', ProductTownSearchAPIView.as_view(), name='searchtown'),
    path('product-catsearch/', ProductCategorySearchAPIView.as_view(), name='searchcat')
]
