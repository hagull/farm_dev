from django.contrib import admin
from .models import TestGcg

@admin.register(TestGcg)
class TestGcgAdmin(admin.ModelAdmin):
    pass
# Register your models here.
