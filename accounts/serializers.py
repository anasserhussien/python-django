from rest_framework.serializers import(

 ModelSerializer, 
 HyperlinkedIdentityField,
 SerializerMethodField

)

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
from django.core.exceptions import ValidationError 


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

