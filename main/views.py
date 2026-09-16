from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ExperienceForm
from main.models import Experience


def show_main(request):
    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "npm": "2506618723",
        "study_program": "S1 Ilmu Komputer",
        "bio": "A Computer Science student at Universitas Indonesia",
    }
    return render(request, "index.html", context)


# 1. Menampilkan Experience (menggunakan deserialize JSON sesuai Tutorial hal. 24)
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


# 2. Form Tambah Experience (Halaman 12-13)
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


# 3. Endpoint JSON Data Delivery (Halaman 21)
def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")


# 4. Hapus Experience (Halaman 24-25)
def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")