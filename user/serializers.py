
from rest_framework import  serializers  #model serializersi import ediyorum.
from django.contrib.auth.models import User #default user modelimizi import ediyoruz
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator #email adresinin tek olması için import ediyoruz.


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2',
                  'email', 'first_name', 'last_name')
       
        #validate overread yaptık. passworlar eşit değilse hata döndür eşitse passwordu döndür.
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs


    def create(self, validated_data): #validated_data dediğimiz,  kullanıcıdan istediğimiz bilgiler.

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )  # (**validated_data) #kısa hali

        user.set_password(validated_data['password'])
        user.save()

        return user
