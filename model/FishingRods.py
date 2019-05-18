from model.FishingShop import FishingShop
from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType

class FishingRods(FishingShop):
     def __init__(self, price, name, masa, material, producer=Producer.ASIA, guarantee=12,
		 color="white", season = Season.ALL_SEASON, fishingSetType = FishingSetType.FISHINGNET, maximumWeight = 0, length = 0):
         super().__init__(price,  name,  masa, material,  producer,  guarantee)
         self.maximumWeight = maximumWeight
         self.length = length

     def __str__(self):
         return "price = " + self.price + ", name = " + self.name + ", masa = " + self.masa + ", material = " + self.material +\
              ", producer = " + self.producer + ", guarantee = " + self.guarantee + ", color = " + self.color + ", season = "\
              + self.season + ", fishingSetType = "  + self.fishingSetType +  ", maximumWeight = " + self.maximumWeight + ", length = " \
                + self.length + "\n"

     def __del__(self):
         print("Delete")