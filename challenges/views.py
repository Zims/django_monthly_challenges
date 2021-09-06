from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december",
}

def index(request):
    list_items = ""    
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        capitlized_month = month.capitalize()
        list_items += f"<li><a href=\"{month_path}\">{capitlized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Month not found")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # = challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month": month})
    except KeyError:
        return HttpResponseNotFound("Month not found")
