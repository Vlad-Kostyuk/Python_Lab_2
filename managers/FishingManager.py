from model.Bait import Bait
from model.FishingShop import FishingShop

class FishingManager:

    def __init__(self, fishing):
        self.fishing = fishing

    def searchByPrice(self, price):
        return list(filter(lambda FishingShop:FishingShop.price == price, self.fishing))

    def sortByPriceUpDown(fishing, sortPrice):
        return sorted(fishing, key = lambda FishingShop: FishingShop.price, reverse=sortPrice)

    def sortByNameUpDown(fishing, sortName):
        return sorted(fishing, key=lambda FishingShop: FishingShop.name, reverse=sortName)

    def searchBySeason(self, season):
        return list(filter(lambda FishingShop:FishingShop.season == season, self.fishing))

    def sortBySeasonUpDown(fishing, sortSeason):
        return sorted(fishing, key=lambda FishingShop: FishingShop.season, reverse=sortSeason)

    def searchByProducer(self, producer):
        return list(filter(lambda FishingShop:FishingShop.producer == producer, self.fishing))

    def sortByProducerUpDown(fishing, sortProducer):
        return sorted(fishing, key=lambda FishingShop: FishingShop.producer, reverse=sortProducer)

    def searchByFishingSetType(self,fishingSetType):
        return list(filter(lambda FishingShop:FishingShop.fishingSetType == fishingSetType, self.fishing))

    def sortByFishingSetTypeUpDown(fishing, sortFishingSetType):
        return sorted(fishing, key=lambda FishingShop: FishingShop.fishingSetType, reverse=sortFishingSetType)