from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class Index(TemplateView):
    '''
    стартовая страница приложения parser_map
    '''
    template_name = 'parser_map/index.html'
