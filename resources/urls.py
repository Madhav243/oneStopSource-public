from django.urls import path

from resources import views

urlpatterns=[

path('',views.index,name='index'),
path('topics',views.viewTopics,name='topicsView'),
path('topics/<int:pk>',views.subtopics,name='get_subtopics'),
path('profile',views.profile,name='profile'),
path('search',views.search,name='search'),
path('subscribe',views.subscribe,name='subscribe'),

path('request_form',views.request_form,name='request_form')


]
