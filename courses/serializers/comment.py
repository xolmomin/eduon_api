from rest_framework.serializers import ModelSerializer

from courses.models import Comment


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()
