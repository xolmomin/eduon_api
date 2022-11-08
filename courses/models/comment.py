from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, IntegerChoices

from shared.django.models import BaseModel


class Comment(BaseModel):
    class RatingChoice(IntegerChoices):
        excellent = 5
        good = 3
        bad = 2

    rating = IntegerField(default=RatingChoice.good, choices=RatingChoice.choices)
    course = ForeignKey('courses.Course', CASCADE)
    author = ForeignKey('auth.User', CASCADE)
    text = CharField(max_length=512)

    class Meta:
        ordering = ('-created_at',)
