from django.shortcuts import render
from .forms import GraphForm
from .models import Graph
from django.http import HttpResponseRedirect	

# Create your views here.
def create_graph(request):
	if request.method == 'POST':
		form = GraphForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/graph/')
	else:
		form = GraphForm()
	return render(request, 'landing.html', {'form': form})

def get_graph(request, graph_id=1):
	return render(request, 'graph.html', {'graph': Graph.objects.get(id=graph_id)})