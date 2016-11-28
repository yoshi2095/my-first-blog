from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *

# Create your views here.

def project_list(request):
	projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'portfolio/project_list.html', {'projects':projects})

def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	return render(request, 'portfolio/project_detail.html', {'project':project})

@login_required
def project_new(request):
	if request.method == "POST":
		form=ProjectForm(request.POST)
		if form.is_valid():
			project=form.save(commit=False)
			project.author = request.user
			#project.published_date = timezone.now()
			project.save()
			return redirect('project_detail', pk=project.pk)
	else:
		form = ProjectForm()
	return render(request, 'portfolio/project_edit.html', {'form':form})

@login_required
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

@login_required
def project_draft_list(request):
	projects= Project.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'portfolio/project_draft_list.html', {'projects':projects})

@login_required
def project_publish(request,pk):
	project = get_object_or_404(Project, pk=pk)
	project.publish()
	return redirect('project_detail', pk=pk)

@login_required
def project_remove(request, pk):
	project = get_object_or_404(Project, pk=pk)
	project.delete()
	return redirect('project_list')

def add_comment_to_project(request,pk):
	post = get_object_or_404(Project, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('project_detail', pk=pk)
	else:
		form=CommentForm()
	return render(request, 'portfolio/add_comment_to_project.html', {'form':form})

@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment,pk=pk)
	comment.approve()
	return redirect('project_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('project_detail', pk=post_pk)


