

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.utils.html import format_html

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name ='دسته بندی'
        verbose_name_plural ='دسته بندی ها'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نویسنده')
    category = models.ManyToManyField(Category, related_name='articles' ,verbose_name='دسته بندی')
    title = models.CharField(max_length=70 ,verbose_name='عنوان')
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(null=True, unique=True)
    pub_date=models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ('-created',)
        verbose_name ='مقاله'
        verbose_name_plural ='مقالات'

    def save(self, force_insert=False):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):

        return reverse('article_app:post_details', kwargs={'slug': self.slug})
    
    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="40px">')
        else:
            return format_html('<h3> تصویری وجود ندارد</h3>')
    show_image.short_description='تصویر مقاله'

    def __str__(self) -> str:
        return f"{self.title} - {self.body[0:30]}"


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
    
    class Meta:
        verbose_name ='نظر'
        verbose_name_plural ='نظرات'


class Message(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='پیام'
        verbose_name_plural ='پیام ها'


class Ticket(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='تیکت'
        verbose_name_plural ='تیکت ها'
        
class Likes(models.Model):
    user=models.ForeignKey(User, verbose_name="کاربر", related_name='likes',on_delete=models.CASCADE)
    article=models.ForeignKey(Article,verbose_name="مقاله", related_name='likes',on_delete=models.CASCADE)
    created_at=models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.article.title}'
    
    class Meta:
        verbose_name ='لایک'
        verbose_name_plural ='لایک ها'
        ordering=('created_at',)
