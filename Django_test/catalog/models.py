from django.db import models
from djrichtextfield.models import RichTextField

class DateTimeStamp(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        abstract = True

class Category(DateTimeStamp):
    name = models.CharField('Назва катергорії', max_length=25, unique=True)
    url = models.URLField('URL', blank=True)
    email = models.EmailField('Email', blank=True)
    description = RichTextField('Опис', blank=True)
    activate = models.BooleanField('Active', default=False)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['name']

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField('Тег', max_length=25, unique=True)
    uuid = models.UUIDField('UUID')

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name



class Goods(DateTimeStamp):
    name = models.CharField('Назва товару', max_length=25, unique=True)
    description = RichTextField('Опис', blank=True)
    activate = models.BooleanField('Active', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    tags = models.ManyToManyField(Tags, related_name='goods_tag')
    image = models.ImageField('Image', upload_to='image', blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return self.name

