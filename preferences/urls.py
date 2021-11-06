from django.conf.urls import url
from django.urls import path
from django.views.static import serve

from preferences import views

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:query_id>/', views.query, name='query'),
    url(r'^(?P<path>.*)$', serve, {'document_root': '/home/sascha/BA/Pref-RL/Pref-RL/videofiles'})
] 