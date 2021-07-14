from django.db import models

class chart(models.Model):
    Country = models.CharField(max_length=100)
    Value = models.CharField(max_length=15)

    def __str__(self):
        return "{}".format(self.Country)