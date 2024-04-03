from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import forms


# Create your views here.

class Index(TemplateView):
    '''
    стартовая страница приложения parser_map
    '''
    template_name = 'parser_map/index.html'


class SearchQuery(TemplateView):
    """
    страница поискового запроса
    """
    template_name = 'parser_map/search_query.html'


class Answer(TemplateView):
    """
    страница ответа на запрос
    """
    template_name = "parser_map/answer.html"
