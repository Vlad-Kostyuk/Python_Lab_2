from model.FishingShop import FishingShop
from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType


class Bait(FishingShop):
    def __init__(self, price=0, name=0, masa=0, material="material", guarantee=12, color="white", producer=Producer.EUROPE, season=Season.ALL_SEASON,
                 fishing_set_type=FishingSetType.FISHINGNET, length=0):
        super().__init__(price, name, masa, material, guarantee, color, producer, season, fishing_set_type)
        self.length = length

    def __str__(self):
        return str(self.price) + " " + str(self.name) + " " + str(self.masa) + " " + str(self.material) + \
           " " + str(self.guarantee) + " " + str(self.color) + str(self.producer) + " " + str(self.season.value) \
           + " " + str(self.fishingSetType.value) + " " + str(self.length)
