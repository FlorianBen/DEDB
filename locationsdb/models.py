from django.db import models

from polymorphic.models import PolymorphicModel

# Create your models here.


class Location(PolymorphicModel):
    """
    Base class of all Location related models.

    Note that this is not a Meta class but please use much as possible derived classes.
    """
    name_text = models.TextField('Location name', max_length=200)

    def code(self) -> str:
        return ''

    def __str__(self) -> str:
        return self.name_text


class Building(Location):
    """
    Define generic Building object.

    Two more specialized classes are available, please use them much as possible.
    """
    building_int = models.IntegerField('Building number', default=0)


class Office(Building):
    """
    An Office is a specialized Building object where people have their offices and works.
    """
    #TODO: Implement.
    pass


class Installation(Building):
    """
    An Installation is a specialized Building object where one or more Experiments are located.

    LIPAc building is an :Installation:.
    """
    #TODO: Implement.
    pass


class Level(Location):
    """
    A Level represents a floor in a :Building:.

    Typicaly the floor 3F is a :Level: of the QST main office.
    """
    level_int = models.IntegerField('Level')
    building_ref = models.ForeignKey(
        Building, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.building_ref.name_text + '>' + self.name_text


class Area(Location):
    """
    An Area represent a subdivision in a :Level:.
    """
    level_ref = models.ForeignKey(
        Level, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.level_ref.__str__() + '>' + self.name_text

class Zone(Location):
    """
    An Zone is an smaller open space inside an :Area:
    """
    area_ref = models.ForeignKey(
        Area, on_delete=models.CASCADE, blank=True, null=True)
    code_text = models.CharField('Code text', max_length=2, blank='True')
    index_int = models.IntegerField('Index')

    def code(self) -> str:
        return self.code_text + str(self.index_int).zfill(2)

    class Meta:
        unique_together = ["code_text", "index_int"]

    def __str__(self) -> str:
        return self.area_ref.__str__() + '>' + self.name_text

class Unit(Zone):
    """
    A Unit is an enclosed space inside a :Zone:.

    Typicaly, a rack or a cubicle is a :Unit:
    """
    def __str__(self) -> str:
        return self.area_ref.__str__() + '>' + self.name_text


class Room(Zone):
    """
    A Room is an enclosed Zone inside an :Area:.

    Office building have many rooms.
    """
    room_number = models.IntegerField('Level')

    def __str__(self) -> str:
        return self.area_ref.__str__() + '>' + self.name_text