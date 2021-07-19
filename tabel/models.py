from django.db import models

# Create your models here.
class tabel(models.Model):
    waktu = models.CharField(max_length=30)
    nama = models.CharField(max_length=50)
    level = models.CharField(max_length=30)
    pesan = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
