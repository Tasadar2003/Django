from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Goods, Tags
from .serializers import CategorySerializer, GoodsSerializer, TagSerializer

from datetime import date
today = date.today()


class CategoryViews(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('id')

class GoodsViews(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.order_by('created')

class TagViews(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tags.objects.order_by('id')
