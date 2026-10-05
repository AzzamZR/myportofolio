from django.urls import path

from main.views import (
    create_experience,
    create_experience_ajax,
    create_project,
    create_project_ajax,
    delete_experience,
    delete_project,
    edit_experience,
    edit_project,
    toggle_star_experience,
    toggle_star_project,
    get_experience_json,
    get_project_json,
    show_experience,
    show_project,
    show_main,
    register,
    login_user,
    logout_user

)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),

    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/edit/<uuid:experience_id>/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),

    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("project/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("api/project/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("project/edit/<uuid:project_id>/", edit_project, name="edit_project"),
    path("project/<uuid:project_id>/star/", toggle_star_project, name="toggle_star_project"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    
]