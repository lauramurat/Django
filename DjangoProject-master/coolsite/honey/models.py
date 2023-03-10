from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Аты')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    brand = models.TextField(blank=True, verbose_name='Бренд аты')
    content = models.TextField(blank=True, verbose_name='Сипаттамасы')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Сурет')
    price = models.CharField(max_length=255, verbose_name='Бағасы')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Құрылған уақыт')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Өзгертілген уақыт')
    is_published = models.BooleanField(default=True, verbose_name='Публикациясы')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категориясы')


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug':self.slug})

    class Meta:
        verbose_name = "Продуктілер"
        verbose_name_plural = "Продуктілер"
        ordering = ['time_create','name']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug':self.slug})

    class Meta:
        verbose_name = "Категориялар"
        verbose_name_plural = "Категориялар"
        ordering = ['id']
