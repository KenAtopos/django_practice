from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def january(request):
#     return HttpResponse("This works!")


# def february(request):
#     return HttpResponse("February")


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "january challenges"
    elif month == "february":
        challenge_text = "february challenge"
    else:
        return HttpResponseNotFound("This month is not supported.")

    return HttpResponse(challenge_text)
