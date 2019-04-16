from django.contrib import admin
from .models import Booth, Company


class BoothInline(admin.TabularInline):
    model = Booth
    fields = ['name', 'contact', 'road_address']


@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'company', 'road_address']
    search_fields = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [
        BoothInline,
    ]
