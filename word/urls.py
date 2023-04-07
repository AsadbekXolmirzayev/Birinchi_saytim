from django.urls import path
from .views import index, detail, category, article_list

app_name = 'word'

urlpatterns = [
    path('', index, name='index'),
    path('category/', category, name='category'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('list/', article_list, name='list'),
]

