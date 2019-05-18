from model.FishingShop import FishingShop
from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType
from model.Sex import Sex
from model.Size import Size

class Clothing(FishingShop):
    def __init__(self, price, name, masa, material, producer=Producer.ASIA, guarantee=12,
		 color="white", season = Season.ALL_SEASON, fishingSetType = FishingSetType.FISHINGNET, size = Size.XL, sex = Sex.MALE):
        super().__init__(price,  name,  masa, material,  producer,  guarantee)
        self.size = size
        self.sex = sex

    def __str__(self):
        return  "price = " + self.price + ", name = " + self.name + ", masa = " + self.masa + ", material = " + self.material +\
              ", producer = " + self.producer + ", guarantee = " + self.guarantee + ", color = " + self.color + ", season = "\
              + self.season + ", fishingSetType = "  + self.fishingSetType + ",size = " + self.size + ", sex = " + self.sex + "\n"
    def __del__(self):
        print("Delete")