from django.shortcuts import render
from datetime import datetime
# Create your views here.
from .forms import ContactForm, PostForm
from .models import Mood, Post


def post2db(request):
    form = PostForm()
    moods = Mood.objects.all()
    message = 'All messages'

    return render(request, 'mform_post2db.html', locals())


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = 'OK'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
        else:
            message = 'NG'
    else:
        form = ContactForm()
    return render(request, 'mform_contact.html', locals())


def index(request):
    now = datetime.now()

    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None

    if urid != None and urpass == '12345':
        verified = True
    else:
        verified = False

    return render(request, 'mform.html', locals())
