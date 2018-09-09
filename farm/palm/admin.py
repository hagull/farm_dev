from django.contrib import admin
from .models import Gcg, Anode, Snode, GcgCctv, AllHouseCctv

@admin.register(Gcg)
class GcgAdmin(admin.ModelAdmin):
    pass
@admin.register(Anode)
class AnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(Snode)
class SnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(GcgCctv)
class GcgCctvAdmin(admin.ModelAdmin):
    pass
@admin.register(AllHouseCctv)
class AllHouseCctvAdmin(admin.ModelAdmin):
    pass

# Register your models here.
