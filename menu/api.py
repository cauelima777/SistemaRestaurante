from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def api_menu_list(request):
    menu_items = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu_items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_menu_create(request):
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'OPTIONS', 'GET'])
def api_menu_update(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'PUT':
        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'OPTIONS':
        return Response(status=200)
    elif request.method == 'GET':
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)

@api_view(['DELETE', 'OPTIONS', 'GET'])
def api_menu_delete(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'DELETE' or request.method == 'GET':
        item.delete()
        return Response(status=204)
    elif request.method == 'OPTIONS':
        return Response(status=200)
