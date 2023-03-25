from django.db import models

from polymorphic.models import PolymorphicModel

# Create your models here.


class GroupSystem(models.Model):
    """
    Group is the higher division in the system classification.
    """
    name_text = models.TextField('Name', max_length=200)
    code_text = models.CharField('Code text', max_length=1, blank='True')

    def __str__(self):
        return self.name_text

class BaseSystem(PolymorphicModel):
    """
    BaseSystem is the base class for the System classification.
    Any :Instance: should be linked to a object that inherit this class. 
    """
    name_text = models.TextField('Name', max_length=200)
    code_text = models.CharField('Code text', max_length=2, blank='True')

    def code(self) -> str:
        return self.code_text

class System(BaseSystem):
    """
    A System represents the different system within a group.
    """
    group_ref = models.ForeignKey(
        GroupSystem, on_delete=models.CASCADE, blank=True, null=True)

    def code(self) -> str:
        return self.group_ref.code_text + self.code_text

    def __str__(self):
        return self.group_ref.__str__() + '>' + self.name_text
    
    
    """
    A SubSystem is a subdivision of a :System:, and may be usefull to use for nested :System:
    """
class SubSystem(BaseSystem):
    system_ref = models.ForeignKey(
        System, on_delete=models.CASCADE, blank=True, null=True)

    def code(self) -> str:
        return self.system_ref.code() + self.code_text

    def __str__(self):
        return self.system_ref.__str__() + '>' + self.name_text
