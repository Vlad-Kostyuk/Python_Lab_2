from managers.FishingManager import FishingManager
from model.FishingShop import FishingShop
from model.Bait import Bait
from model.Clothing import Clothing
from model.FishingNet import FishingNet
from model.Producer import Producer
from model.Season import Season
from model.FishingSetType import FishingSetType

fishingShop = FishingShop(2000, "Hg123", 2, "metal", Producer.USA, 12, "Black", Season.WINTER,
                          FishingSetType.FISHINGNET)
bait_object = Bait(2500, "LL-123", 0.5, "metal",  24, "green", Producer.EUROPE, Season.SUMMER, FishingSetType.FISHINGRODS, 12)
clothing = Clothing(4500, "T-Shirt", 0.1, "hlopk", Producer.USA, 12, "white", Season.SUMMER, FishingSetType.CLOTHING,
                    )
fishingNet = FishingNet(1000, "sitka", 3, "plasmasa", Producer.ASIA, 12, "blue", Season.ALL_SEASON,
                        FishingSetType.FISHINGNET)
fishing_list = [clothing, fishingShop, bait_object]
fishingManager_obj = FishingManager(fishing_list)

print(*fishing_list, sep="\n")
print("-----------------")
new_list = fishingManager_obj.sort_fishing_list_by_price(False)
print(*new_list, sep="\n")


