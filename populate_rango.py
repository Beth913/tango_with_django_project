import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/'},
         {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/'},
         {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/'} ]
    
    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
         {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
         {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/'} ]
    
    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
        'url':'http://flask.pocoo.org'} ]

    websites = {'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
        'Other Frameworks': {'pages': other_pages} }

    for website, website_data in websites.items():
        w = add_website(website)
        for p in website_data['pages']:
            add_page(w, p['title'], p['url'])

    for w in Category.objects.all():
        for p in Page.objects.filter(category=w):
            print(f'- {w}: {p}')


def add_page(website, title, url, views=0):
    p = Page.objects.get_or_create(category=website, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_website(name):
    w = Category.objects.get_or_create(name=name)[0]
    w.save()
    return w

if __name__ == '__main__':
    print('Staring Rango population script . . .')
    populate()