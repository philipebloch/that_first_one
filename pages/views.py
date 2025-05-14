from django.http import HttpResponse # HttpResponse allows us to send a http message to the borwser, such as html or text.
from django.views.generic import TemplateView #the template view already has all the logci we need. Our task is only to specify the template's name

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'