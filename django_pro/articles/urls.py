from django.urls import path
from . import views
from django.urls import include
app_name = 'articles'
urlpatterns = [
    path('',views.article_list,name="list"),
    path('create',views.article_create,name="create"),
    path('<slug>/',views.article_detail,name="detail"),
    path('my_articles',views.my_articles,name = 'my_articles'),
    path('search',views.search,name='search'),
]