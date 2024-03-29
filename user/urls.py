from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('products/', views.products, name='products'),
    path('products/new/', views.products_new, name='products_new'),
    path('productsedit/<int:id>', views.productsedit, name='productsedit'),
    path('productsdelete/<int:id>', views.productsdelete, name='productsdelete'),
    path('comments/', views.comments, name='comments'),

]
