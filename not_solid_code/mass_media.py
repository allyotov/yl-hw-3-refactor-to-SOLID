from places import Place
from heroes import SuperHero


def create_news(hero: SuperHero, place: Place):
    print(f'{hero.name} saved the {place.name}!')
