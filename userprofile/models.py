from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    serviceprovider = models.BooleanField(null=True, blank=True)
    opensat = models.TimeField(null=True)
    closesat = models.TimeField(null=True)
    duration = models.IntegerField(null=True,blank=True)
    noappointments = models.IntegerField(null=True,blank=True)
    visitfee = models.IntegerField(null=True,blank=True)
    occupation = models.TextField(max_length=500, blank=True)
    city = models.TextField(blank=True, max_length=50)
    address = models.TextField(default='248, 18, shivaji park shabhaji nagar pune-411019')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created , **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





