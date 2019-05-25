from model.FishingShop import FishingShop
from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType

class FishingRods(FishingShop):
    def __init__(self, price=0, name="name", material="material", producer=Producer.EUROPE, guarantee=0,
         color="color", season=Season.ALL_SEASON, fishing_set_type=FishingSetType.FISHINGNET, maximum_weight=0,
                  length=0):
         super().__init__(self, price, name, material, producer, guarantee, color, season, fishing_set_type)
         self.maximumWeight = maximum_weight
         self.length = length

    def __str__(self):
        return str(self.price) + " " + str(self.name) + " " + str(self.masa) + " " + str(self.material) + \
            " " + str(self.guarantee) + " " + str(self.color) + str(self.producer) + " " + str(self.season.value) \
            + " " + str(self.fishingSetType.value) + " " + str(self.maximumWeight) + " " + str(self.length)
