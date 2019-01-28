from django.urls import path
from . import views
from entity import views


urlpatterns = [
	path('', views.entity_list, name='entity_list'),
	path('query/', views.entity_query, name='entity_query'),
]