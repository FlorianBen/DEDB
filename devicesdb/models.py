from django.db import models

from taggit.managers import TaggableManager

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
        (NOTFORNEW, 'Not recommanded for new desing'),
        (OBSOLETE, 'Obsolete'),
        (UNKNOWN, 'Unknown'),
    ]

    COTS = 'CO'
    CUSTOM = 'CU'
    OTHERS = 'OT'
    SOLUTION_CHOICES = [
        (COTS, 'Commercial off-the-shelf'),
        (CUSTOM, 'Custom made'),
        (OTHERS, 'Other/Unknow'),
    ]

    name_text = models.CharField(max_length=200)

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

    entry_date = models.DateField('Entry date', auto_now_add=True)
    lastupdate = models.DateField('Last update', auto_now=True)

    tags = TaggableManager()

    def __str__(self) -> str:
        return self.name_text


class Manufacturer(models.Model):
    """
    The Manufacturer model handle the information about
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

    name_text = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=UNKNOWN)
    new_manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    website_url = models.URLField('Manufacturer website', blank=True)

    entry_date = models.DateField('Entry date', auto_now_add=True)
    lastupdate = models.DateField('Last update', auto_now=True)

    def __str__(self) -> str:
        return self.name_text