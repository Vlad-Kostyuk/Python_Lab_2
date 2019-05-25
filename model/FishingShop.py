from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType


class FishingShop:
    def __init__(self, price=0, name=0, masa=0, material="material", guarantee=12, color="white", producer=Producer.EUROPE, season=Season.ALL_SEASON,
                 fishing_set_type=FishingSetType.FISHINGNET):
        self.price = price
        self.name = name
        self.masa = masa
        self.material = material
        self.producer = producer
        self.guarantee = guarantee
        self.color = color
        self.season = season
        self.fishingSetType = fishing_set_type

    def __str__(self):
        return str(self.price) + " " + str(self.name) + " " + str(self.masa) + " " + str(self.material) + \
           " " + str(self.guarantee) + " " + str(self.color) + str(self.producer) + " " + str(self.season.value) \
           + " " + str(self.fishingSetType.value)