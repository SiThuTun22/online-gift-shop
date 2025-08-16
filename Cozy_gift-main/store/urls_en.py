from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('home/', views.home_en, name='home_en'),
    path('navbar/', views.navbar_en, name='navbar'),
    path('base/', views.base_en, name='base'),
    path('suggestion/', views.suggestion_en, name='suggestion'),
    path('product/', views.products_en, name="product"),
    path('about-us/', views.about_us_en, name="about_us"),
    path('category/<str:foo>/', views.category_en, name='category_en'),
    path('coming/', views.coming_soon_en, name='coming'),
    path('search/', views.search_en, name='search_en'),
    path('product-detail/<int:pk>/', views.product_detail_en, name="product_detail"),
    path('login/', views.login_user_en, name='login'),
    path('signup/', views.register_user_en, name="register"),
    path('logout/', views.logout_user_en, name="logout"),
    path('update_user/', views.update_user_en, name="update_user"),
    path('update_info/', views.update_info_en, name="update_info"),
    path('update_password/', views.update_password_en, name="update_password"),
    path('filter-data/', views.filter_data_en, name='filter_data__en'),

    # Flower landing page
    path('flowerlanding/', views.flowerlanding_en, name='flowerlanding_en'),

    # Flower detail page (using string name)
    path('flower/<str:name>/', views.flower_detail_en, name='flower_detail_en'),

    # Removed the overly broad '<str:flower_name>/' to avoid URL conflicts
]
