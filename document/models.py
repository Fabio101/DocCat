from django.db import models
import uuid

# Create your models here.

class Document(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	catalogue = models.ForeignKey('catalogue.Catalogue')
        name = models.CharField(max_length=120, unique=True)
	description = models.TextField(max_length=2000)
	document = models.FileField(upload_to='document/')
        date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
        date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

        def __unicode__(self):
                return self.name
