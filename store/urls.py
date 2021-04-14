from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('fashion/', views.fashion, name="fashion"),
    path('books/', views.books, name="books"),
    path('electronics/', views.electronics, name="electronics"),
    path('accessories/', views.accessories, name="accessories"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('search/', views.search, name='search'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:product_id>', views.product, name="product"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),

]
