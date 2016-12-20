from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserGroup(models.Model):
	group_id=models.CharField(max_length=10)
	group_name =models.CharField(max_length=10)


def _unicode_(self):
 	return self.groupid

def _str_(self):
 	return self.groupid


class UserData(models.Model):
	group_id =models.CharField(max_length=10)
	contact_name=models.CharField(max_length=15)
	mobile_number=models.CharField(max_length=12)


def _unicode_(self):
 	return self.groupid

def _str_(self):
 	return self.groupid

