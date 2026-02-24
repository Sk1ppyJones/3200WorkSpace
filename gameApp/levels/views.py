from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

game_levels = {
    "the-forest": "A beautiful forest with dark shadows surrounding you",
    "the-mountain": "A dark looming mountain casting its shadown down on the town",
    "the-sewers": "A gross dungeon like place for you to search, watch out for the turtles",
    "the-desert": "A dry sandy desert with cacti ents lurking, in ever search of you."
}


def index(request):
    list_items = ""
    levels = list(game_levels.keys())
    print(levels)

    for level in levels:
        clean_label = level.replace("-", " ").title()
        # TODO: Create URL
        level_path = reverse('level-name', args=[level])
        list_items += f'<li><a href="{level_path}">{clean_label}</a></li>'

    return HttpResponse(list_items)


def level_by_number(request, level_num):
    levels = list(game_levels.keys())
    if level_num > len(levels) or level_num <= 0:
        return HttpResponseNotFound('<h1>Level Not Found</h1>')

    redirect_level = levels[level_num - 1]
    redirect_path = reverse("level-name", args=[redirect_level])

    return HttpResponseRedirect(redirect_path)


def level_details(request, level_name):

    try:
        description = game_levels[level_name]
        return HttpResponse(f'<h1>Level: {level_name.replace('-', ' ').title()}</h1><p>{description}</p>')
    except KeyError:
        return HttpResponseNotFound('<h1>Level Not Found</h1>')
