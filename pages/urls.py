from django.urls import path #path function allows us to create urls within the application
from .views import homePageView #we're importinh the homePageView function from the .views file to be able to map it to url, that we will specify in this code.

urlpatterns = [ #is a list where we store all of the urls our app has, and map them to the right function that will triger http messages with the right data, and templates.
    path('', homePageView) #the path function takes the url, and the function to map it with. 
]