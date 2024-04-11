from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from selenium.common import TimeoutException

from . import forms
from django.core.cache import cache
from . import parser_map
from . import test_date


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
    success_url = reverse_lazy('parser_map:answer')

    def post(self, request, *args, **kwargs):
        result = super(SearchQuery, self).post(request, *args, **kwargs)
        text_of_find = request.POST.get("find")  # получили поисковый запрос, который надо передать на парсер

        flag = 1
        result_date = [{
            "address": "не установленно",
            "phone": "не установленно"
        }, ]
        while bool(flag) and flag < 3:
            try:
                result_date = parser_map.ParseYandexMap(search_query=text_of_find)()  # ответ парсера на запрос
                flag = False
            except TimeoutException:
                flag += 1

        # result_date = test_date.data
        # print(result_date)
        cache.set('result_date', result_date)
        return result


class Answer(TemplateView):
    """
    страница ответа на запрос
    """
    template_name = "parser_map/answer.html"

    def get_context_data(self, **kwargs):
        result_date = cache.get('result_date')
        context = super().get_context_data(**kwargs)
        context['result_date'] = result_date
        cache.delete('result_date')
        return context
