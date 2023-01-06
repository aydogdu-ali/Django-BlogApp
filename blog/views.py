from django.shortcuts import render

from.models import Category, Blog
from .serializers import CategorySerializers,BlogSerializers


from rest_framework.viewsets import ModelViewSet

#viewset modelini kullanıyorum
class CategoryView(ModelViewSet):  #crud işlemleri
    queryset = Category.objects.all() # kullanacağımız veri tablosu
    serializer_class = CategorySerializers # kullanacağımız veri tablosuna ait serializer
    
    filterset_fields = ['name'] #modelde yazdığımız fields göre hangisi olacaksa onu yazıyoruz.

    


#viewset modelini kullanıyorum
class BlogView(ModelViewSet): ##crud işlemleri
    queryset = Blog.objects.all() # kullanacağımız veri tablosu
    serializer_class = BlogSerializers # kullanacağımız veri tablosuna ait serializer
    # filterset_fields = ['category__name'] # CATEGORY NAME İNE GÖRE FİLTRELEME YAPMAK İÇİN

    filterset_fields = ['category'] #modelde yazdığımız fields göre hangisi olacaksa onu yazıyoruz.

    search_fields= ['title', 'content'] #modelde yazdığımız fields göre hangisi olacaksa onu yazıyoruz.