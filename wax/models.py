from django.db import models
from django.utils.encoding import smart_unicode
from djangoratings.fields import RatingField
from django.contrib.auth.models import User

# Create your models here.

WAX_TYPE = (
        ('E', 'Oil'),
        ('S', 'Shatter'),
        ('W', 'Wax'),
        ('O', 'Other',)
)

HIGH_TYPE = (
        ('ID', 'Indica'),
        ('IDH', 'Indica Dom. Hybrid'),
        ('HY', 'Hybrid'),
        ('SDH', 'Sativa Dom. Hybrid'),
        ('SV', 'Sativa'),
)
SOLVENT_TYPE = (
        ('B', 'Butane'),
        ('C', 'CO2'),
)


class Wax(models.Model):
        name            = models.CharField(max_length=200)
        slug            = models.SlugField(unique=True)
        dispensary      = models.ForeignKey('Dispensary')
        type            = models.CharField(max_length=1, choices=WAX_TYPE)
        high            = models.CharField(max_length=3, choices=HIGH_TYPE)
        solvent         = models.CharField(max_length=1, choices=SOLVENT_TYPE)
        pricepergram    = models.IntegerField(max_length=3, blank=False)
        description     = models.TextField(blank=True)
        wax_pic         = models.ImageField(upload_to="images/waxthumbs/")
	rating 		= RatingField(range=5) # 5 possible rating values, 1-5

        def __unicode__(self):
                return self.name

class Dispensary(models.Model):
        name            = models.CharField(max_length=200)
        slug            = models.SlugField(unique=True)
        city            = models.CharField(max_length=100)
        address         = models.CharField(max_length=200)
        phone           = models.BigIntegerField(max_length=11, blank=True)
        website         = models.CharField(max_length=200)
        email           = models.EmailField(blank=True)
        description     = models.TextField(blank=True)
	map_addr	= models.CharField(max_length=200, blank=True, default='', help_text='Please input like: City, Street Address')
        disp_pic        = models.ImageField(upload_to="images/dispthumbs")
	rating 		= RatingField(range=5) # 5 possible rating values, 1-5

        def __unicode__(self):
                return self.name

