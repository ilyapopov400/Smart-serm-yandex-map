from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from . import forms


# Create your views here.

class Index(TemplateView):
    '''
    стартовая страница приложения parser_map
    '''
    template_name = 'parser_map/index.html'


class SearchQuery(FormView):
    """
    страница поискового запроса
    """
    template_name = 'parser_map/search_query.html'
    form_class = forms.FormSearchQuery
    success_url = reverse_lazy('parser_map:index')

    def post(self, request, *args, **kwargs):
        result = super(SearchQuery, self).post(request, *args, **kwargs)
        text_of_find = request.POST.get("find")
        print(text_of_find)  # получили поисковый запрос, который надо передать на парсер
        return result


class Answer(TemplateView):
    """
    страница ответа на запрос
    """
    template_name = "parser_map/answer.html"
