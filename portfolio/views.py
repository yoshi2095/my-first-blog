from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Project
from .forms import ProjectForm

# Create your views here.

def project_list(request):
	projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'portfolio/project_list.html', {'projects':projects})

def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	return render(request, 'portfolio/project_detail.html', {'project':project})

def project_new(request):
	if request.method == "POST":
		form=ProjectForm(request.POST)
		if form.is_valid():
			project=form.save(commit=False)
			project.author = request.user
			project.published_date = timezone.now()
			project.save()
			return redirect('project_detail', pk=project.pk)
	else:
		form = ProjectForm()
	return render(request, 'portfolio/project_edit.html', {'form':form})

def project_edit(request, pk):
	project = get_object_or_404(Project, pk=pk)
	if request.method == "POST":
		form=ProjectForm(request.POST,instance=project)
		if form.is_valid():
			project=form.save(commit=False)
			project.author = request.user
			project.published_date = timezone.now()
			project.save()
			return redirect('project_detail', pk=project.pk)
	else:
		form=ProjectForm(instance=project)
	return render(request, 'portfolio/project_edit.html', {'form':form})
