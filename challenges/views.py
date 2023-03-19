from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not support")
