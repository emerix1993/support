# POKEMONS = {}
#
#
# # @dataclass
# # class Pokemon:
# #     id: int
# #     name: str
# #     height: int
# #     weight: int
# #     base_experience: int
#
# def pokemon_handler(request, name):
#     if request.method == 'GET':
#         return get_pokemon(request, name)
#     elif request.method == 'DELETE':
#         return delete_pokemons(request, name)
#     else:
#         return HttpResponse(status=405)
#
#
# def get_pokemon(request, name):
#     try:
#         pokemon = POKEMONS[name]
#         data = asdict(pokemon)
#     except KeyError:
#         url = settings.POKEAPI_BASE_URL + f"/{name}"
#         response = requests.get(url)
#         data = response.json()
#         POKEMONS[name] = data
#
#
#     pokemon_info = {"id": data["id"],
#                     "name": name,
#                     "height": data["height"],
#                     "weight": data["weight"],
#                     "baseExperience": data["base_experience"]}
#     fields = ("id", "name", "height", "weight", "baseExperience")
#     result = {field: pokemon_info[field] for field in fields}
#     return HttpResponse(content_type="application/json", content=json.dumps(result))
#
#
# def all_pokemons(request):
#     return HttpResponse(content_type="application/json", content=json.dumps(POKEMONS))
#
#
# def delete_pokemons(request, name):
#     if name in POKEMONS:
#         del POKEMONS[name]
#         return HttpResponse(content_type="application/json", content=json.dumps({"message": "Pokemon deleted"}))
#     else:
#         return HttpResponse(content_type="application/json", content=json.dumps({"message": "Pokemon not found"}))
