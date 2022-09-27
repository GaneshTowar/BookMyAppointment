from django.db import models
from django.contrib.auth.models import User
# Create your models here
class regis(models.Model):
    appointment_opt = models.CharField(max_length=50)
    cl = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,related_name='cl')
    sp = models.ForeignKey(User,to_field='id',on_delete=models.CASCADE,related_name='sp')
    date = models.DateField(null=True)
    time = models.TextField(null=True)
    stat = models.CharField(max_length=50)
