from django.urls import path
from . import views

urlpatterns = [
    # Category List View
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    
    # Home Category List View (Random order of 5 categories)
    path('categories/home', views.HomeCategoryList.as_view(), name='home-category-list'),
    
    # Brand List View
    path('brands/', views.BrandList.as_view(), name='brand-list'),
    
    # Product List View (Random order of 20 products)
    path('', views.ProductList.as_view(), name='product-list'),
    
    # Popular Products List View (Filter products with ratings between 4.0 and 5.0)
    path('popular/', views.PopularProductsList.as_view(), name='popular-product-list'),
    
    # Product List by Clothes Type (Filter products based on clothes type)
    path('byType/', views.ProductListByClothesType.as_view(), name='product-list-by-clothes-type'),
    
    # Similar Products (Filter products based on category)
    path('recommendations/', views.SimilarProducts.as_view(), name='similar-product-list'),
    
    path('category/', views.FilterProductByCategory.as_view(), name='filter-product-by-category'),
    
    # Search Product by Title (Filter products by title)
    path('search/', views.SearchProductByTitle.as_view(), name='search-product-by-title'),
]
