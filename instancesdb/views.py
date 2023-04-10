from django.shortcuts import render
from django.http import Http404

from .models import Instance

def index(request):
    lastupdate = Instance.objects.order_by('-lastupdate')[:5]
    context = {
        'lastupdate': lastupdate,
    }
    return render(request, 'instances/index.html', context)


def detail(request, instance_id):
    try:
        instance = Instance.objects.get(pk=instance_id)
    except Instance.DoesNotExist:
        raise Http404("Instance does not exist")
    return render(request, 'instances/detail.html', {'instance': instance})

# Create your views here.
