from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for 2 hours every day!",
    "april": "Drink 2 cup water every morning!",
    "may": "Not to drink tea!",
    "june": "Don't use mobile phone every saturday!",
    "july": "Help your parents on their work!",
    "august": "Talk with one stranger every single day!",
    "september": "Not to use any social media except for learning!",
    "october": "Listen educational podcast every morning!",
    "november": "Spend time with yourself for 1 hour!",
    "december": "Exercise and meditate every morning!"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\"><h3>{month.capitalize()}</h3></a></li>"
    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    else:
        return HttpResponse(response_data)
