from atexit import register
from django import template
from datetime import datetime



register=template.Library()

@register.simple_tag


def time_now():
    #showing time now in navbar
    
    return datetime.now().strftime("%Y-%m-%d ")