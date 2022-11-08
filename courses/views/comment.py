from rest_framework.viewsets import ModelViewSet

from courses.models import Comment
from courses.serializers import CommentModelSerializer


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

