from django import forms
from .models import Manufacturer


class ManufacturerForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class ReferenceForm(forms.Form):
    name_text = forms.CharField(label="Name of the reference", max_length=200)
    ref_manufacturer_text = forms.CharField(label="Reference", max_length=200)
    status = forms.URLField(label="Status")
    solution = forms.CharField(label="Solution type")
    website_url = forms.URLField(label="Website URL")
    
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(), initial=Manufacturer.objects.first())
