from django.shortcuts import render
from dataclasses import dataclass
from typing import List, Dict, Optional
from django.http import HttpRequest, HttpResponse


@dataclass
class Team:
    name: str
    description: str
    members: List[str]


TeamsDict = Dict[str, Team]
TeamDetailParam = str
OptionalTeamParam = Optional[TeamDetailParam]

teams: TeamsDict = {
    "Management": Team(
        name="Management",
        description="Description for Management - They check cleaning supplies",
        members=["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Mathew"],
    ),
    "Procurement": Team(
        name="Procurement",
        description="Description for Procurement - They give us sandwiches",
        members=["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"],
    ),
    "Documentation": Team(
        name="Documentation",
        description="Description for Documentation - They are the best out of everyone else",
        members=[
            "Conner",
            "Kaleigh",
            "Blair",
            "Mina",
            "Jay",
            "Joshua",
            "Kayleah",
        ],
    ),
    "Community": Team(
        name="Community",
        description="Description for Community - They get told by Shawn what to do",
        members=["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
}


def team_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, "base.html", {"teams": teams})


def team_detail_view(request: HttpRequest, team_name: TeamDetailParam) -> HttpResponse:
    team: Optional[Team] = teams.get(team_name)
    return render(request, "team_detail.html", {"team": team})


def start_view(request: HttpRequest) -> HttpResponse:
    return render(request, "base.html")


def team_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, "team_list.html", {"teams": teams})
