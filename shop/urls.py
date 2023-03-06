from django.urls import path, include

from . import views

urlpatterns = [
    path('shop/', views.list_item, name='shop'),     # name - is endpoint
    path('shop/<int:item_id>/', views.detail_item, name='shop' ),

]