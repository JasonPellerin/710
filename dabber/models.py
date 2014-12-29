from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#from annoying.fields import AutoOneToOneField
#from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Dabber(models.Model):
        user            = models.OneToOneField(User, related_name="profile")
        birthday        = models.DateField()
        name            = models.CharField(max_length=100)
        email           = models.EmailField(max_length=100)
        dbr_pic         = models.ImageField(upload_to="images/dabberthumbs/", blank=True)	

        def __unicode__(self):
                return self.name


class UserProfile(models.Model):

        user            = models.OneToOneField(User, verbose_name=(u"user"), on_delete=models.CASCADE,)



        def __unicode__(self):
                return self.name
