from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType

class FishingShop:
    def __init__(self, price, name, masa, material, producer=Producer.ASIA, guarantee=12,
		 color="white", season = Season.ALL_SEASON, fishingSetType = FishingSetType.FISHINGNET):
        self.price = price
        self.name = name
        self.masa = masa
        self.material = material
        self.producer = producer
        self.guarantee = guarantee
        self.color = color
        self.season = season
        self.fishingSetType = fishingSetType

    def __str__(self):
        return "price = " + self.price + ", name = " + self.name + ", masa = " + self.masa + ", material = " + self.material +\
              ", producer = " + self.producer + ", guarantee = " + self.guarantee + ", color = " + self.color + ", season = "\
              + self.season + ", fishingSetType = "  + self.fishingSetType +"\n"
    def __del__(self):
        print("Delete")