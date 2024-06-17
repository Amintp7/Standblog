from nntplib import ArticleInfo
from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html



class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده')
    title = models.CharField(max_length=50,verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    category = models.ManyToManyField(Category,related_name='articles',verbose_name='دسته بندی')#related_name=classname + s
    image = models.ImageField(upload_to='images/articles',blank=True,null=True,verbose_name='عکس')
    slug = models.SlugField(null = True,blank=True,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True,verbose_name='وضعیت')
    published = models.BooleanField(default=True,verbose_name='انتشار')



    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.slug = slugify(self.title)
        super(Article,self).save()
    
    def get_absolute_url(self):
        return reverse('blog_app:article_details',args=[self.slug])
    
    class Meta:
        ordering=('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        

    def __str__(self):
        return f"{self.title}"
    
    def test(cls):
            from blog_app.models import Article
            pass
    
    def show_image(self):

        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        return format_html('<h3 style="color: red;">تصویر ندارد</h3>')
    show_image.short_description = 'تصویر'





class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]
    
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها  '
        
        

class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes',verbose_name='کاربر')
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='likes',verbose_name='مقاله')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"
    
    
    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created',)
