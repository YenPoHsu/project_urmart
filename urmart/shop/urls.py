from django.urls import path

from . import views

urlpatterns = [
    # shop: show products and content of shopping cart
    # path('', views.index, name ='index'),
    path('', views.ShopMainView.as_view(), name='shopmain'),

    # add product order to shopping cart
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:product_id>/create2/',
         views.OrderCreate2, name='order_create2'),

    # delete order from shopping cart
    path('order/<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),

]
