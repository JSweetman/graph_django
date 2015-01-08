from django.shortcuts import render
from .forms import GraphForm
from django.http import HttpResponseRedirect	

# Create your views here.
def make_graph(request):
	if request.method == 'POST':
		form = GraphForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/success/')
	else:
		form = GraphForm()
	return render(request, 'base.html', {'form': form})