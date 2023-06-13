from django.db import models

from taggit.managers import TaggableManager
from simple_history.models import HistoricalRecords

# Create your models here.


class Reference(models.Model):
    """
    A reference is an item in a catalog. A reference represent a purely virtual device.
    """
    ACTIVE = 'AC'
    NOTFORNEW = 'NN'
    OBSOLETE = 'OB'
    UNKNOWN = 'UN'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (NOTFORNEW, 'Not recommended for new design'),
        (OBSOLETE, 'Obsolete'),
        (UNKNOWN, 'Unknown'),
    ]

    COTS = 'CO'
    CUSTOM = 'CU'
    OTHERS = 'OT'
    SOLUTION_CHOICES = [
        (COTS, 'Commercial off-the-shelf'),
        (CUSTOM, 'Custom made'),
        (OTHERS, 'Other/Unknown'),
    ]

    name_text = models.CharField(max_length=200, blank=False)

    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    ref_manufacturer_text = models.CharField(max_length=200, blank='True')
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=UNKNOWN)
    solution = models.CharField(
        max_length=2, choices=SOLUTION_CHOICES, default=COTS)
    EoL_date = models.DateField('End of Life date', blank=True, null=True)
    website_url = models.URLField('Webpage of the item', blank=True)
    picture = models.ImageField(
        'Picture', upload_to='reference_picture', blank=True)

    entry_date = models.DateField('Entry date', auto_now_add=True)
    last_update = models.DateField('Last update', auto_now=True)

    tags = TaggableManager()
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name_text


class Manufacturer(models.Model):
    """
    The Manufacturer model handle the information about the manufacturer producer/seller of a device.
    """
    ACTIVE = 'AC'
    ACQUIRED = 'AQ'
    LIQUIDATION = 'LQ'
    UNKNOWN = 'UN'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (ACQUIRED, 'Part of a new company'),
        (LIQUIDATION, 'Not active anymore'),
        (UNKNOWN, 'Unknown'),
    ]

    PRIVATE_INSTITUTE = 'PR'
    PUBLIC_INSTITUTE = 'PU'
    COMPANY = 'CP'
    TYPE_CHOICES = [
        (COMPANY, 'Private company'),
        (PRIVATE_INSTITUTE, 'Private institute'),
        (PUBLIC_INSTITUTE, 'Public institute'),
        (UNKNOWN, 'Unknown'),
    ]

    name_text = models.CharField(
        'Name', max_length=200, unique=True, blank=False)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=UNKNOWN)
    type = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=UNKNOWN)
    new_manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    website_url = models.URLField('Manufacturer website', blank=True)
    logo_file = models.ImageField(
        'Logo', upload_to='manufacturer_logos', blank=True)

    entry_date = models.DateField('Entry date', auto_now_add=True)
    last_update = models.DateField('Last update', auto_now=True)

    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name_text
