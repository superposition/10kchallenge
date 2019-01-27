from django.urls import path
from . import views
#from Entity import views

urlpatterns = [
	path('', views.entity_list, name='entity_list')
]