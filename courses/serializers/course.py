from rest_framework.serializers import ModelSerializer

from courses.models import Category, Course


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('slug',)


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ()
