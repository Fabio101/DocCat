from django.db import models
from django.contrib.auth.models import Group
import uuid

# Create your models here.

class Catalogue(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	group = models.ForeignKey(Group, default=1, null=True)
	name = models.CharField(max_length=20, unique=True, null=False)
	description = models.TextField(max_length=2000)
	date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
	date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		return self.name
