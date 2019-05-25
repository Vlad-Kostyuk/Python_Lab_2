from model.FishingShop import FishingShop

class FishingManager:

    def __init__(self, fishing_list):
        self.fishing_list = fishing_list

    def sort_fishing_list_by_price(self, reverse):
        return sorted(self.fishing_list, key=lambda fishing: fishing.price, reverse=reverse)