from django.shortcuts import render

from.models import Category, Blog
from .serializers import CategorySerializers,BlogSerializers


from rest_framework.viewsets import ModelViewSet

#crud işlemleri için kullanıcı login ise yetki vermek için import ettim.
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#özel yazdığımız permission u import ediyoruz.
from .permissions import IsAdminOrReadOnly

#viewset modelini kullanıyorum
class CategoryView(ModelViewSet):  #crud işlemleri
    queryset = Category.objects.all() # kullanacağımız veri tablosu
    serializer_class = CategorySerializers # kullanacağımız veri tablosuna ait serializer
    
    filterset_fields = ['name'] #modelde yazdığımız fields göre hangisi olacaksa onu yazıyoruz.

    permission_classes = [IsAdminOrReadOnly]
    


#viewset modelini kullanıyorum
class BlogView(ModelViewSet): ##crud işlemleri
    queryset = Blog.objects.all() # kullanacağımız veri tablosu
    serializer_class = BlogSerializers # kullanacağımız veri tablosuna ait serializer
    # filterset_fields = ['category__name'] # CATEGORY NAME İNE GÖRE FİLTRELEME YAPMAK İÇİN

    filterset_fields = ['category'] #modelde yazdığımız fields göre hangisi olacaksa onu yazıyoruz.

    search_fields= ['title', 'content'] #modelde yazdığımız fields göre hangisi olacaksa onu yazıyoruz.

    #eger login ise Crud işlemlerini yapabilir değilse sadece get yapar.
    permission_classes = [IsAuthenticatedOrReadOnly]


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

#kullanıcı çıkış yaptığında token silme
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message":"Token Deleted"})