from rest_framework.serializers import(

 ModelSerializer, 
 HyperlinkedIdentityField,
 SerializerMethodField

)

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
from django.core.exceptions import ValidationError 

from django.db.models import Q

class UserCreateSerializer(ModelSerializer):

    # why adding email while it's already added by default?
    # to make it required field
    email = serializers.EmailField(
    label = "Email Adress"
    )
    email2 = serializers.EmailField(
    label = 'Confirm Email'
    )
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'email2'
        ]

        extra_kwargs = {"password":
                    {
                        "write_only": True
                    },
                    "email2":
                    {
                        "write_only": True
                    }}

    def validate(self, data):
        pass
        # we can validate anything here also

    def validate_email(self, value):

        data =self.get_initial()

        if User.objects.filter(email = data.get("email")).exists():
            raise ValidationError("This user is already registered")

        if data.get('email2') == value:
            return value
        raise ValidationError("Emails must match")

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username = username,
            email = email,
        )

        # below function for encrypting password
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



class UserLoginSerializer(ModelSerializer):

    # why adding email while it's already added by default?
    # to make it required field
    username = serializers.CharField()
    token = serializers.CharField(
        allow_blank = True,
        read_only = True
    )
    # email = serializers.EmailField(
    # label = "Email Adress"
    # )
    class Meta:
        model = User
        fields = [
            'username',
            #'email',
            'password',
            'token'
        ]

        extra_kwargs = {"password":
                    {
                        "write_only": True
                    }}

    def validate(self, data):
        user = User.objects.filter(
            username = data.get("username")
        ).distinct()

        if user.exists() and user.count() ==1:
            user = user.first()
        else:
            raise ValidationError("The username you entered is not exist")
        

        if not user.check_password(data.get("password")):
            raise ValidationError("Incorrect password please check again")

        data["token"] = "Random Token"

        return data