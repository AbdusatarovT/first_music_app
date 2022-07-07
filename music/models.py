from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.SlugField(primary_key=True) # Создание главного поля

    def __str__(self):
        return self.title


class Music(models.Model):
    COUNTRY = (
        ('KG', 'Кыргызстан'), # KG запишется в БД
        ('KZ', 'Казахстан')
    )
    author = models.ManyToManyField(User) # связь многие ко многим, необходимо импортировать from django.contrib.auth.models import User
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='music')
    duration = models.IntegerField() 
    country = models.CharField(max_length=30, choices=COUNTRY) # указывает страну из списка доступных
    created_at = models.DateField(auto_now_add=True)  # Указывает время когда было добавлено

    def __str__(self):
        return f'{self.title} {self.category}'