from django.urls import path
from .views import MenuCategoryListView

urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name='menu-categories')
    
]