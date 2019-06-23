from django.shortcuts import render
from django.http import HttpResponse
import random


def about(request):
    quotes = [
        "Two wrongs don't make a right.",
        "The pen is mightier than the sword.",
        "When in Rome, do as the Romans."
        "The squeaky wheel gets the grease.",
        "When the going gets tough, the tough get going.",
        "No man is an island.",
        "Fortune favors the bold."

    ]
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())
