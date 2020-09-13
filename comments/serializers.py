from rest_framework.serializers import(

 ModelSerializer, 
 HyperlinkedIdentityField,
 SerializerMethodField

)
from .models import Comment

class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'