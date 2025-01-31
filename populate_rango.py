import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 97},
         {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 60},
         {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 13} ]
    
    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 156},
         {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 41},
         {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 78} ]
    
    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views': 27},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': 48} ]

    websites = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    for website, website_data in websites.items():
        w = add_website(website, website_data['views'], website_data['likes'])
        for p in website_data['pages']:
            add_page(w, p['title'], p['url'], p['views'])

    for w in Category.objects.all():
        for p in Page.objects.filter(category=w):
            print(f'- {w}: {p}')

def add_page(website, title, url, views):
    p = Page.objects.get_or_create(category=website, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_website(name, views, likes):
    w = Category.objects.get_or_create(name=name)[0]
    w.views = views
    w.likes = likes
    w.save()
    return w

if __name__ == '__main__':
    print('Staring Rango population script . . .')
    populate()