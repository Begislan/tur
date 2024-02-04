import datetime

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class TurModel(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    full = RichTextUploadingField()  # CKEditor Rich Text Field
    klass = models.BooleanField(default=False)
    img = models.ImageField()

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title