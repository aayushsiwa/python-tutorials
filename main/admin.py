from django.contrib import admin
from .models import Tutorial,TutorialCategory,TutorialSeries

# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    # fields = ["published", "title", "content"]
    fieldsets = [
        ("Title/Date", {"fields": ["title", "published"]}),
        ("URL", {"fields": ["slug"]}),
        ("Series", {"fields": ["series"]}),
        ("Content", {"fields": ["content"]}),
    ]
    # formfield_overrides = {models.TextField: {"widget": QuillField()}}



admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)