from django.db import models

# Create your models here.
class logs(models.Model):
    time = models.CharField(max_length=30)
    Name = models.CharField(max_length=50)
    level = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self) -> str:
        return super().__str__()