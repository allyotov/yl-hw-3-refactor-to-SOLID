from antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def fire_a_gun(self):
        print('PIU PIU')

    def attack(self):
        self.fire_a_gun()

class KickMixin:
    def ultimate(self):
        print('Bump')

class LazerMixin:
    def ultimate(self):
        print('Wzzzuuuup!')

class Superman(LazerMixin, SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def kick(self):
        return 'Kick'
