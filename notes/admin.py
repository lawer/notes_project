from django.contrib import admin

# Register your models here.
from notes.models import Alumne, Nota

admin.site.register(Alumne)
admin.site.register(Nota)
