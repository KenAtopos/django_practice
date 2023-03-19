from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Learn Django",
    "february": "Learn React",
    "march": "Develop a personal project",
    "april": "Contribute to an open-source project",
    "may": "Improve your algorithm skills",
    "june": "Learn a new programming language",
    "july": "Build a web application",
    "august": "Learn about databases",
    "september": "Learn about APIs",
    "october": "Prepare for a coding interview",
    "november": "Participate in Hacktoberfest",
    "december": "Create a portfolio website",
}


def index(request):
    list_items = ""

    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        item = f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"
        list_items += item

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not support")
