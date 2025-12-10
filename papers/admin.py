from django.contrib import admin
from .models import Paper, Level, Subject

# Register your models here.
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Paper)