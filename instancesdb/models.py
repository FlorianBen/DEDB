from django.db import models

from polymorphic.models import PolymorphicModel

from cataloguedb.models import Reference
from locationsdb.models import Location
from systemsdb.models import BaseSystem
# Create your models here.

# TODO: Move the code to the Device/Spare


class Instance(PolymorphicModel):
    """
    An Instance defines an physical object wrt to a reference in the catalog.
    """
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default='', blank=True,
                                 null=True)

    sn_internal_text = models.CharField(
        'SN internal', max_length=200, blank='True')
    sn_manufacturer_text = models.CharField(
        'SN manufacturer', max_length=200, blank='True')

    order_text = models.CharField(
        'Order number', max_length=200, blank='True')

    reception_date = models.DateField('Reception date')

    entry_date = models.DateField('Entry date', auto_now_add=True)
    lastupdate = models.DateField('Last update', auto_now=True)


class Device(Instance):
    """
    A Device represents an operating :Instance:
    """
    system_ref = models.ForeignKey(BaseSystem, on_delete=models.CASCADE, default='', blank=True,
                                   null=True)
    ref = models.ForeignKey(Reference,
                            on_delete=models.CASCADE,
                            blank=False,
                            null=False)

    code_text = models.CharField('Code text', max_length=2, blank='True')
    index_instance = models.PositiveIntegerField(
        'Internal index', blank=True, null=True)

    install_date = models.DateField('Installation date')

    def __str__(self) -> str:
        return self.system_ref.code() + self.code_text + self.index_instance.__str__().zfill(3) + 'L' + self.location.code()


class Spare(Instance):
    """
    A Spare represent an Instance that is actually stored.

    A Spare should must as possible have a linked :Device:.
    """
    device_ref = models.ForeignKey(Device, on_delete=models.CASCADE,
                                   blank=False)

    def __str__(self):
        return self.device_ref.__str__() + 'S'
