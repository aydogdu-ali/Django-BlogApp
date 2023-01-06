from django.shortcuts import render


from django.contrib.auth.models import User #default user modelini import ettik.

from.serializers import RegistrationSerializer

#concrete Methodi ile class yazma
from rest_framework.generics import CreateAPIView #sadece oluşturma işlemi için kullanırız.



class RegisterView(CreateAPIView):
    queryset= User.objects.all() #modelimizi yazıyoruz.
    serializer_class = RegistrationSerializer #serializers tanımlıyoruz.