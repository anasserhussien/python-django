from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
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

    class Meta:
        model = Post
        fields = "__all__"

        # fields = [
        #     'title',
        #     'slug',
        #     'content',

        # ]