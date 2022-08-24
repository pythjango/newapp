from django.urls import path
from.import views
urlpatterns=[
    path('home',views.seller_home),
    path('cart',views.seller_cart),
    path('order',views.seller_order),

]