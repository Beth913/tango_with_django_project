from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #return HttpResponse('<a href="/rango/about/">About</a>')
    return render(request, 'rango/index.html', context=context_dict)

    

#def about(request):
 #   return HttpResponse('<a href="/rango/">Index</a>')
