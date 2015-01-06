from django import forms
from .models import Graph

class GraphForm(forms.ModelForm):

	class Meta:
		model = Graph
		fields = ('title', 'graph_type', 'csv_file')