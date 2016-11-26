from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Project

# Create your views here.

def project_list(request):
	projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'portfolio/project_list.html', {'projects':projects})

def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	return render(request, 'portfolio/project_detail.html', {'project':project})

