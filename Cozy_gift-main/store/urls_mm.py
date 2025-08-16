from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('home/', views.home_mm, name='home_mm'),
    # add other Myanmar routes here...
    path('navbar/' , views.navbar_mm, name='navbar'),
    path('base/' , views.base_mm, name='base'), 
    path('suggestion/', views.suggestion_mm, name='suggestion'),
    path('product/',views.products_mm,name="product"),
    path('about-us/', views.about_us_mm, name="about_us"),
    path('category/<str:foo>/', views.category_mm, name='category_mm'),
    path('coming/', views.coming_soon_mm, name='coming'),
    path('search/', views.search_mm, name='search_mm'),
    # store/urls_mm.py
# ...
    path('product-detail/<int:pk>/', views.product_detail_mm, name="product_detail"),
# ...
    path('login/', views.login_user_mm, name='login'),
    path('signup',views.register_user_mm,name="register"),
    path('logout/',views.logout_user_mm,name="logout"),
    path('update_user/',views.update_user_mm,name="update_user"),
    path('update_info/',views.update_info_mm,name="update_info"),
    path('update_password/',views.update_password_mm,name="update_password"),
    path('filter-data/', views.filter_data_mm, name='filter_data__mm'),
    path('flowerlanding/', views.flowerlanding_mm, name='flowerlanding_mm'),

   
    
    #path('flowerLanding/',views.flowerLanding,name="flowerLanding"),
   path('flower/<str:name>/', views.flower_detail_mm, name='flower_detail_mm'),


    
    
]
