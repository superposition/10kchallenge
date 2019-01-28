from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Entity
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def entity_list(request):
	entities = Entity.objects.all()
	return render(request, 'entity/entity_list.html', {'entities': entities})

def entity_query(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            entities = form.save(commit=False)
            entities.author = request.user
            entities.published_date = timezone.now()
            entities.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/entity_query.html', {'form': form})