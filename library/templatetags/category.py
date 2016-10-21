from django import template
from django.utils.safestring import mark_safe

from library.models import Category

register = template.Library()

@register.simple_tag
def show_category(pl):
    category = Category.objects.all()
    
    if pl == 'nav':
        res = ''
        for cat in category:
            res += '<li><a href="/library/' + cat.name + '/">' + cat.name.capitalize() + '</a></li>'
        
        return mark_safe(res)
    else:
        return 'Error'
