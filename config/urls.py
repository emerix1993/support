"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json
# from dataclasses import dataclass, asdict
import requests
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.conf import settings

POKEMONS = {}


# @dataclass
# class Pokemon:
#     id: int
#     name: str
#     height: int
#     weight: int
#     base_experience: int

def pokemon_handler(request, name):
    if request.method == 'GET':
        return get_pokemon(request,name)
    elif request.method == 'DELETE':
        return delete_pokemons(request,name)
    else:
        return HttpResponse(status=405)


def get_pokemon(request, name):
    if name in POKEMONS:
        data = POKEMONS[name]
    else:
        url = settings.POKEAPI_BASE_URL + f"/{name}"
        response = requests.get(url)
        data = response.json()
        POKEMONS[name] = data

    pokemon_info = {"id": data["id"],
                    "name": name,
                    "height": data["height"],
                    "weight": data["weight"],
                    "baseExperience": data["base_experience"]}
    fields = ("id", "name", "height", "weight", "baseExperience")
    result = {field: pokemon_info[field] for field in fields}
    return HttpResponse(content_type="application/json", content=json.dumps(result))


def all_pokemons(request):
    return HttpResponse(content_type="application/json", content=json.dumps(POKEMONS))


def delete_pokemons(request, name):
    if name in POKEMONS:
        del POKEMONS[name]
        return HttpResponse(content_type="application/json", content=json.dumps({"message": "Pokemon deleted"}))
    else:
        return HttpResponse(content_type="application/json", content=json.dumps({"message": "Pokemon not found"}))


urlpatterns = [
    path('admin/', admin.site.urls),
    path("pokeapi/<str:name>/", get_pokemon),
    path("pokeapi/pokemons", all_pokemons),
    path("pokeapi/delete/<str:name>", delete_pokemons)
]
