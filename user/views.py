from django.shortcuts import render


from django.contrib.auth.models import User #default user modelini import ettik.

from.serializers import RegistrationSerializer

#concrete Methodi ile class yazma
from rest_framework.generics import CreateAPIView #sadece oluşturma işlemi için kullanırız.



class RegisterView(CreateAPIView):
    queryset= User.objects.all() #modelimizi yazıyoruz.
    serializer_class = RegistrationSerializer #serializers tanımlıyoruz.




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

#kullanıcı çıkış yaptığında token silme

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message":"Token Deleted"})