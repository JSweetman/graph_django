from django.db import models
from time import time

# Create your models here.
def get_upload_file_name(instance, filename):
	return "graphs/%s_%s" % (str(time()).replace('.','_'), filename)

class Graph(models.Model):
	GRAPH_TYPES=(('line', 'Line'),
		('pie', 'Pie'),
		('hist', 'Histogram'))

	title = models.CharField(max_length=30)
	graph_type = models.CharField("Type", max_length=10, choices=GRAPH_TYPES)
	csv_file = models.FileField(upload_to=get_upload_file_name)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title