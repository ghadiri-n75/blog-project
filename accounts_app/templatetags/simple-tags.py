from atexit import register
from django import template

from article_app.models import Article


register=template.Library()

@register.simple_tag


def article_count():
    #counting the number of total article in web page
    
    counter=Article.objects.count()
    return counter


