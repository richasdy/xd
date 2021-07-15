from django.db import models

class chart(models.Model):
    Country = models.CharField(max_length=100)
    Value = models.CharField(max_length=15)

    def __str__(self):
        return "{}".format(self.Country)

class streamgraph(models.Model):
    year = models.IntegerField()
    Amanda = models.IntegerField()
    Ashley = models.IntegerField()
    Betty = models.IntegerField()
    Deborah = models.IntegerField()
    Dorothy = models.IntegerField()
    Helen = models.IntegerField()
    Linda = models.IntegerField()
    Patricia = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()

class density(models.Model):
    Price = models.CharField(max_length=100)
    #Value = models.CharField(max_length=15)

    def __str__(self):
        return "{}".format(self.Price)