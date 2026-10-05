from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        
from django.views.decorators.http import require_POST
import datetime

from main.forms import ExperienceForm, ProjectForm
from main.models import Experience, Project


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    
    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / cookie not found')
    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "npm": "2506618723",
        "study_program": "S1 Ilmu Komputer",
        "bio": "A Computer Science student at Universitas Indonesia",
        "last_login" : last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    
    is_editor = request.user.groups.filter(name='Editor').exists() if request.user.is_authenticated else False
    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
        "is_edit" : False,
    }
    return render(request, "experience_form.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "thumbnail": experience.thumbnail,
                "is_ongoing": experience.is_ongoing,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
    return redirect("main:show_experience")

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
        "is_edit" : True,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

def show_project(request):
    title_query = request.GET.get("title", "").strip()

    is_editor = request.user.groups.filter(name='Editor').exists() if request.user.is_authenticated else False
    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
        "is_edit" : False,
    }
    return render(request, "project_form.html", context)


def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "category": project.category,
                "thumbnail": project.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Proyek berhasil dihapus!")
    return redirect("main:show_project")

@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_project")

    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "form": form,
        "is_edit" : True,
    }
    return render(request, "project_form.html", context)

@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")
