from django.contrib import admin
from .models import Category,Element,Comments,Quiz

# Register your models here.

admin.site.register(Category)
admin.site.register(Element)
admin.site.register(Comments)
admin.site.register(Quiz)

admin.site.site_header = 'Gestionnaire de site'