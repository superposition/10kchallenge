from django.urls import path
from . import views
from entity import views


urlpatterns = [
	path('', views.entity_query, name='entity_list'),
	path('list/', views.entity_list, name='entity_list'),
	path('query/', views.entity_query, name='entity_query'),
	path('detail/<sym>/', views.entity_detail, name="entity_detail"),
]