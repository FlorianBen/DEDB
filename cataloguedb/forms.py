from django import forms
from .models import Manufacturer


class ManufacturerForm(forms.Form):
    your_name = forms.CharField(
        label="Name of the manufacturer", max_length=100)
    website_url = forms.URLField(label="Website URL")
    status = forms.URLField(label="Status")
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(), initial=Manufacturer.objects.first())


class ReferenceForm(forms.Form):
    name_text = forms.CharField(
        label="Name of the reference", max_length=200, required=True)
    ref_manufacturer_text = forms.CharField(
        label="Reference", max_length=200, required=True)
    status = forms.URLField(label="Status")
    solution = forms.CharField(label="Solution type")
    website_url = forms.URLField(label="Website URL")
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(), initial=Manufacturer.objects.first())
