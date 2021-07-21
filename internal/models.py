from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.utils import timezone

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
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return super().__str__()

class TableModel(models.Model):
    username = models.CharField(max_length = 20)
    email =  models.CharField(max_length = 50)
    password = models.CharField(max_length = 16)

    published = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "{}".format(self.username)

class UserLog(models.Model):
    activity = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2} - {3}'.format(self.activity, self.username, self.ip, self.timestamp)

    def __str__(self):
        return '{0} - {1} - {2} - {3}'.format(self.activity, self.username, self.ip, self.timestamp)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    now = timezone.now()
    UserLog.objects.create(activity='user_logged_in', ip=ip, username=user.username, timestamp=now)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    now = timezone.now()
    UserLog.objects.create(activity='user_logged_out', ip=ip, username=user.username, timestamp=now)


@receiver(user_login_failed)
def user_login_failed_callback(sender, request, credentials, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    now = timezone.now()
    UserLog.objects.create(activity='user_login_failed', ip=ip, username=credentials.get('username', None), timestamp=now)