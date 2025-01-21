# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    user name = models.CharField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    full name = models.CharField(max_length=255, null=True, blank=True)
    phone number = models.CharField(max_length=255, null=True, blank=True)
    is active = models.BooleanField()
    is stuff = models.BooleanField()
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Dealer(models.Model):

    #__Dealer_FIELDS__
    dealer code = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Dealer_FIELDS__END

    class Meta:
        verbose_name        = _("Dealer")
        verbose_name_plural = _("Dealer")


class Product Group(models.Model):

    #__Product Group_FIELDS__
    product group name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product Group_FIELDS__END

    class Meta:
        verbose_name        = _("Product Group")
        verbose_name_plural = _("Product Group")


class Product(models.Model):

    #__Product_FIELDS__
    product name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    product group = models.ForeignKey(Product Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")



#__MODELS__END
