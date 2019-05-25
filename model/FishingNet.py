from model.FishingShop import FishingShop
from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType

class FishingNet(FishingShop):
    def __init__(self, price=0, name="name", material="material", producer=Producer.EUROPE, guarantee=0,
                 color="color", season=Season.ALL_SEASON, fishing_set_type=FishingSetType.FISHINGNET, width=0,
                 legth=0, form="овал"):
        super().__init__(price, name, material, producer, guarantee, color, season, fishing_set_type)
        self.width = width
        self.legth = legth
        self.form = form

    def __str__(self):
        return str(self.price) + " " + str(self.name) + " " + str(self.masa) + " " + str(self.material) + \
           " " + str(self.guarantee) + " " + str(self.color) + str(self.producer) + " " + str(self.season.value) \
           + " " + str(self.fishingSetType.value) + " " + str(self.width) + " " + str(self.legth) + " " + str(self.form)