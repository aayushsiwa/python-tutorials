from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField
# from tinymce.models import HTMLField


# Create your models here.


class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class TutorialSeries(models.Model):
    series = models.CharField(max_length=200)
    category = models.ForeignKey(
        TutorialCategory,
        default=1,
        verbose_name="Category",
        on_delete=models.SET_DEFAULT,
    )
    summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.series


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()
    published = models.DateTimeField("date published", default=timezone.now())
    # series = models.ForeignKey(
    #     TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT
    # )
    series = models.ForeignKey(
        TutorialSeries,
        default=None,
        blank=True,
        null=True,
        verbose_name="Series",
        on_delete=models.SET_NULL,
    )
    slug = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.title
