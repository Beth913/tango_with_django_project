from django.shortcuts import render
from django.http import HttpResponse
#from rango.models import Category

def index(request):
    #category_list = Category.objects.order_by(-likes)[:5]
    #context_dict = {}
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Click here!<a href='/rango/about/'>About</a>")


    

#def about(request):
    #return HttpResponse("Bye there<a href='/rango/'>Index</a>")
