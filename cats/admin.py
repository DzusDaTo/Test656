from django.contrib import admin
from .models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'fur_length', 'user')
    search_fields = ('name', 'breed', 'user__username')
    list_filter = ('fur_length',)
    ordering = ('name',)
    fields = ('name', 'age', 'breed', 'fur_length', 'user')
    readonly_fields = ('user',)

