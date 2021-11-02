from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:query_id>/', views.query, name='query')
]