from django.shortcuts import render

# Create your views here.
def make_graph(request):
	return render(request, 'base.html')