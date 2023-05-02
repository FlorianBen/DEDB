from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.db.utils import IntegrityError

from .models import Reference, Manufacturer
from .forms import ManufacturerForm, ReferenceForm
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


def reference_add(request):
    form = ReferenceForm()
    context = {'form': form}
    return render(request, 'catalogue/reference_add.html', context)


def index_manufacturers(request):
    lastupdate = Manufacturer.objects.order_by('-lastupdate')[:20]
    context = {
        'lastupdate': lastupdate,
    }
    return render(request, 'catalogue/index_manufacturers.html', context)


def detail_manufacturers(request, instance_id):
    try:
        instance = Manufacturer.objects.get(pk=instance_id)
    except Manufacturer.DoesNotExist:
        raise Http404("Instance does not exist")
    return render(request, 'catalogue/detail_manufacturers.html', {'instance': instance})


def manufacturer_add(request):
    return render(request, "catalogue/manufacturer_add.html")


def add_manufacturer(request):
    name = request.POST.get('name')
    website = request.POST.get('website')
    status = request.POST.get('status')

    try:
        manu = Manufacturer.objects.create(name_text=name, website_url=website, status=status)
    except IntegrityError:
        raise HttpResponse('<div class="alert alert-danger" role="alert" id="add-result">Internal error</div>')

    return HttpResponse('<div class="alert alert-success" role="alert" id="add-result">The Manufacturer has been added to the database</div>')

def add_reference(request):
    name = request.POST.get('name_text')
    ref_manufacturer = request.POST.get('ref_manufacturer_text')
    status = request.POST.get('status')

    manu = Reference.objects.create(
        name_text=name, status=status)

    return HttpResponse('<div class="alert alert-success" role="alert" id="add-result">The Manufacturer has been added to the database</div>')



def update_status(request):

    return HttpResponse('The Manufacturer has been added to the database')
