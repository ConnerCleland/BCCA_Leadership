from django.urls import path
from app import views

urlpatterns: list[path] = [
    path("", views.team_list_view, name="team_list"),
    path("<str:team_name>/", views.team_detail_view, name="team_detail"),
    path("start/", views.start_view, name="start"),
]
