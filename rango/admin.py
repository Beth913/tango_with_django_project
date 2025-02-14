from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

#categories handling
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)

#pages handling
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)

#user handling
admin.site.register(UserProfile)