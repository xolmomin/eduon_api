from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from courses.models import Category, Course
from courses.serializers import CategoryModelSerializer, CourseModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    parser_classes = (MultiPartParser, )
    serializer_class = CourseModelSerializer
