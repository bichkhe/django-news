from django import template
from boards.models import Category

register = template.Library()

@register.filter(name='show_mainmenu')
def show_mainmenu():
    categories = Category.objects.all()
    return {'categories': categories}
