from django.db import models


# Create your models here.
class Notice(models.Model):
	subject = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
#table name change
class Meta:
	db_table='notice'