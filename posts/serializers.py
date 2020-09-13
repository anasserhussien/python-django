from rest_framework.serializers import(

 ModelSerializer, 
 HyperlinkedIdentityField,
 SerializerMethodField

)
from .models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [

            'title',
            'content'
        ]



class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

        # fields = [
        #     'title',
        #     'slug',
        #     'content',

        # ]

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'list',
        lookup_field = 'slug'
    )
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

        # fields = [
        #     'title',
        #     'slug',
        #     'content',

        # ]
    def get_user(self, object):
        return object.user.username
    # this method is based on SerializerMethodField
    # which is coustomize some fields
    # before sending to the views
