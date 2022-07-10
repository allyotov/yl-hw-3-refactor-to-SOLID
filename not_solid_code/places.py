#DIP (Dependency Inversion)
from abc import ABC, abstractmethod


class Place(ABC):
    name = 'Place'
    @abstractmethod
    def get_villian(self):
        print('In {} ...'.format(self.name))


class Kostroma(Place):
    name = 'Kostroma'

    def get_villian(self):
        super().get_villian()
        print('Orcs hid in the forest')
        

class Tokyo(Place):
    name = 'Tokyo'

    def get_villian(self):
        super().get_villian()
        print('Godzilla stands near a skyscraper')
