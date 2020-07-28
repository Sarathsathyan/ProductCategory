from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('category_edit/<int:id>',views.CategoryEdit,name='category_edit'),
    path('product_edit/<int:id>', views.productEdit, name='product_edit')
    ]
