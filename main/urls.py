from django.urls import path

from main.views import (
    create_experience,
    create_project,
    delete_experience,
    delete_project,
    edit_experience,
    edit_project,
    get_experience_json,
    get_project_json,
    show_experience,
    show_project,
    show_main,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),

    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/edit/<uuid:experience_id>/", edit_experience, name="edit_experience"),

    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/project/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("project/edit/<uuid:project_id>/", edit_project, name="edit_project"),
]