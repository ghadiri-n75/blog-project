from atexit import register
from turtle import title
from django.contrib import admin
from . import models
# Register your models here.


class FilterByTitle(admin.SimpleListFilter):
    title: str= 'کلید های پرتکرار'
    parameter_name: str='title'
    
    def lookups(self, request, model_admin):
        return{
            ('programing','جنکو'),
            ('python','پایتون'),
        }
    def queryset(self, request, queryset) :
        if self.value():
            return queryset.filter(title__icontains=self.value())
        
@admin.register(models.Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','created','show_image']
    list_filter=("published",FilterByTitle)
    


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Ticket)
admin.site.register(models.Likes)
