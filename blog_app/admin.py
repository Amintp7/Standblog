from django.contrib import admin
from .models import Article,Category,Comment,Message
from . import models

class CommentInLine(admin.TabularInline):
    model = models.Comment

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','status','show_image')
    list_editable = ('title','status',)
    list_filter = ('status',)
    inlines = (CommentInLine,)


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)