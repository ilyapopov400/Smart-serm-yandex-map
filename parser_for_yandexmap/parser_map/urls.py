from django.urls import path
from . import views

app_name = 'parser_map'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('search-query/', views.SearchQuery.as_view(), name='search-query'),  # страница поискового запроса
    path('answer/', views.Answer.as_view(), name='answer'),  # страница ответа на запрос

]
