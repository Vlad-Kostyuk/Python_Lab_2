from model.FishingShop import FishingShop
from model.Bait import Bait
from model.Clothing import Clothing
from model.FishingNet import FishingNet
from model.Producer import Producer
from model.Season import Season
from  model.FishingSetType import FishingSetType
from  model.Size import Size
from model.Sex import Sex
from managers.FishingManager import FishingManager

fishingShop = FishingShop(2000, "Hg123", 2, "metal", Producer.USA, 12, "Black", Season.WINTER, FishingSetType.FISHINGNET)
bait = Bait(2500, "LL-123", 0.5, "metal", Producer.EUROPE, 24, "green", Season.SUMMER, FishingSetType.FISHINGRODS, 0.2)
clothing = Clothing(4500, "T-Shirt", 0.1, "hlopk", Producer.USA, 12, "white", Season.SUMMER, FishingSetType.CLOTHING, Size.S, Sex.FEMALE)
fishingNet = FishingNet(1000, "sitka", 3, "plasmasa", Producer.ASIA, 12, "blue", Season.ALL_SEASON, FishingSetType.FISHINGNET, 3, 2, "kletka")
fishing_list = [fishingShop, bait, clothing, fishingNet]
print(fishing_list)
print("-----------------")
fishingManager = FishingManager(fishing_list)
print(FishingManager.searchByPrice(1200))
print("-----------------")
print(fishingManager.sortBySeasonUpDown(sortSeason=True))
print("-----------------")
print(fishingManager.sortBySeasonUpDown(sortSeason=False))