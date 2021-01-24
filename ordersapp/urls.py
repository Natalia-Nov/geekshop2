from django.conf.urls import url

import ordersapp.views as ordersapp
from django.urls import path

app_name = "ordersapp"

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='orders'),
    path('create/', ordersapp.OrderCreate.as_view(), name='order_create'),
]
