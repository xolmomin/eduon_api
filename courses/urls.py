from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses.views import CourseModelViewSet, CategoryModelViewSet, CommentModelViewSet

router = DefaultRouter()
router.register('course', CourseModelViewSet, 'course')
router.register('category', CategoryModelViewSet, 'category')
router.register('comment', CommentModelViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls)),
]
