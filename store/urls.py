from django.urls import path
from . import views

urlpatterns=[
    path('',views.store,name='store'),    
    path('cart/',views.cart,name='cart'),    
    path('checkout/',views.checkout,name='checkout'),    
    path('update_item/',views.updateItem,name='update_item'),    
    path('process_order/',views.processOrder,name='process_order'),    
    path('view_product/<int:pk>',views.viewProduct,name='view_product'),    
    path('login/',views.login_request,name='login'),    
    path('signup/',views.register,name='register'),
    path("logout", views.logout_request, name="logout"),
]