from rest_framework.serializers import ModelSerializer
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