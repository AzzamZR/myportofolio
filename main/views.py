from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ExperienceForm, ProjectForm, SECRET_PASSCODE
from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "npm": "2506618723",
        "study_program": "S1 Ilmu Komputer",
        "bio": "A Computer Science student at Universitas Indonesia",
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience_list = [exp.object for exp in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "experience_list": experience_list,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        input_passcode = request.POST.get("secret_passcode")
        if input_passcode == SECRET_PASSCODE:
            experience.delete()
            messages.success(request, "Pengalaman berhasil dihapus!")
        else:
            messages.error(request, "PIN salah! Gagal menghapus experience.")
    return redirect("main:show_experience")

def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def show_project(request):
    json_response = get_project_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    project_list = [prj.object for prj in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "project_list": project_list,
        "title_query": title_query,
    }
    return render(request, "project.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
    }
    return render(request, "project_form.html", context)


def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    project_json = serializers.serialize("json", projects)
    return HttpResponse(project_json, content_type="application/json")


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        input_passcode = request.POST.get("secret_passcode")
        if input_passcode == SECRET_PASSCODE:
            project.delete()
            messages.success(request, "Proyek berhasil dihapus!")
        else:
            messages.error(request, "PIN salah! Gagal menghapus proyek.")
    return redirect("main:show_project")

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_project")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
    }
    return render(request, "project_form.html", context)