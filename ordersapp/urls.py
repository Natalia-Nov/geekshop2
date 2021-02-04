from django.conf.urls import url

import ordersapp.views as ordersapp
from django.urls import path

app_name = "ordersapp"

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='orders'),
    path('create/', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    path('update/<pk>/', ordersapp.OrderUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
    path('detail/<pk>/', ordersapp.OrderDetail.as_view(), name='order_read'),
    path('forming/<pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),

]

