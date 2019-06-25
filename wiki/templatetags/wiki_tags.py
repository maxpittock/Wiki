from django import template
import re

wikiWordV2 = re.compile(r"\[\[([A-Za-z0-9_]+)\]\]")
register = template.Library()

#filter the characters allowed within the title
@register.filter
def wikify(text):
    return wikiWordV2.sub(r'''
    <a href="/wiki/\1/">\1</a>
    ''', text)
