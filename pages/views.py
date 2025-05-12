from django.http import HttpResponse # HttpResponse allows us to send a http message to the borwser, such as html or text.

def homePageView(request): #we're creating a view function that will take the request object which is a http request sent by the browser, like typing in a URL. 
    return HttpResponse('Hello, World!') #using the imported module to respond with a http response, we use the httpResponse function, where it's argument is the value that the http response contains. in this case it's simple hello world.
