from django.urls import path
from .views import ItemView

#Viewset ke liye as_view dictionary 
item_list = ItemView.as_view({
    'get':'list',    #GET -> list items(with search +pagination)
    'post':'create', #POST ->create new item
    'put':'update',  #put ->update item by ID
})

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('items/<int:pk>/',item_list,name='item-update'),
]