from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Items
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(viewsets.ViewSet):
    """
    A ViewSet for listing,searching and creating items.
    Provides:
    ->list(): Get With optinal search filter
    ->post() or create(): POST to add a new item
    """
    pagination_class = MenuItemPagination

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        """
        Handle Get  request to list or serach items.
        otional query parameter: ?search=<name>
        """
        query = request.query_params.get('search',None)
        if query:
            Items = Items.objects.filter(name__icontains=query)
        else:
            Items = Items.objects.all()

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(Items,request)
        serializer = ItemSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

class MenuItemPagination(PageNumberPagination):
        page_size = 5
        page_size_query_param = 'page_size'
        max_page_size=50

