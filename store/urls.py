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
    path('user/<int:user_id>', views.user, name='user'),
    path('update_item/', views.updateItem, name="update_item"),
    path('update_fav/', views.updateFav, name="update_fav"),
    path('cancel_order/', views.cancelOrder, name="cancel_order"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:product_id>', views.product, name="product"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("history/", views.history, name="history"),
]
