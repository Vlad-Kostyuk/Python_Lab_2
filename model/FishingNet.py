from model.FishingShop import FishingShop
from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType

class FishingNet(FishingShop):
    def __init__(self, price, name, masa, material, producer=Producer.ASIA, guarantee=12,
		 color="white", season = Season.ALL_SEASON, fishingSetType = FishingSetType.FISHINGNET, width = 0,
                 legth = 0, form = "овал"):
        super().__init__(price,  name,  masa, material,  producer,  guarantee)
        self.width = width
        self.legth = legth
        self.form = form

    def __str__(self):
        return "price = " + self.price + ", name = " + self.name + ", masa = " + self.masa + ", material = " + self.material +\
              ", producer = " + self.producer + ", guarantee = " + self.guarantee + ", color = " + self.color + ", season = "\
              + self.season + ", fishingSetType = "  + self.fishingSetType + ", width = " + self.width + ", length = " + self.legth + \
               ", form = " + self.form + "\n"

    def __del__(self):
        print("Delete")