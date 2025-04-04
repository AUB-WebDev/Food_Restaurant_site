from django import template
import random

register = template.Library()

@register.simple_tag
def random_number(num1=1, num2=5):
    return random.randint(num1, num2)