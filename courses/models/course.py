from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, SET_NULL, SlugField, ForeignKey, BooleanField, TextChoices, ImageField
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django.models import BaseModel


class Category(MPTTModel):
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', SET_NULL, 'subcategory', blank=True, null=True)
    slug = SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            count = Category.objects.filter(slug=self.slug).count()
            self.slug = f'{self.slug}-{count}'
        super().save(*args, **kwargs)


class Course(BaseModel):
    class LanguageChoice(TextChoices):
        EN = 'en'
        RU = 'ru'
        UZ = 'uz'

    author = ForeignKey('auth.User', SET_NULL, null=True, blank=True)
    category = ForeignKey('courses.Category', SET_NULL, null=True, blank=True)
    image = ImageField(upload_to='courses/')
    language = CharField(max_length=5, choices=LanguageChoice.choices, default=LanguageChoice.UZ)
    is_free = BooleanField(default=False)
    name = CharField(max_length=255)
    key_word = ArrayField(CharField(max_length=255), null=True, blank=True)

    @property
    def comments_count(self):
        return self.comment_set.count()

    @property
    def course_rating(self):
        ratings = self.comment_set.values_list('rating', flat=True)
        return sum(ratings) // len(ratings)

    class Meta:
        ordering = ('-created_at', )
