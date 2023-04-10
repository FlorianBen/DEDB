from django.shortcuts import render
from django.http import Http404

from .models import Reference
# Create your views here.


def index(request):
    lastupdate = Reference.objects.order_by('-lastupdate')[:5]
    context = {
        'lastupdate': lastupdate,
    }
    return render(request, 'catalogue/index.html', context)

def detail(request, instance_id):
    try:
        instance = Reference.objects.get(pk=instance_id)
    except Reference.DoesNotExist:
        raise Http404("Instance does not exist")
    return render(request, 'catalogue/detail.html', {'instance': instance})
