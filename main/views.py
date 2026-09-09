from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Azzam Zawawi Al Rasyid",
        "npm": "2506618723",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at Universitas Indonesia"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Azzam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)