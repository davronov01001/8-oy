from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    def __str__(self):
        return self.title
    
    @property
    def video_url(self):
        return self.file.url if self.file else None