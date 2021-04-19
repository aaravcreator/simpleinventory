from django.urls import path,include
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('add_product', views.addproduct_view, name='addproduct'),
    path('customer/<str:cust_id>', views.customer_view, name='customer'),
    path('add_order',views.add_order,name='add_order'),
    path('update_order/<str:order_id>',views.update_order,name='update_order'),
    path('add_customer',views.addcustomer,name='add_customer'),
    
    
    path('test', views.test_view, name='test'),
    ]


