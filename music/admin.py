from django.contrib import admin
from music.models import Category, Music # необходимо импортировать models
# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'category', 'created_at'] # вывод всех значений в разных таблицах
    list_filter = ['category'] # фильтрация по категориям
    search_fields = ['id']

admin.site.register(Category)
admin.site.register(Music, MusicAdmin)
