from django.shortcuts import render
from .models import Entity

# Create your views here.
def entity_list(request):
	entities = Entity.objects.all()
	return render(request, 'entity/entity_list.html', {'entities': entities})