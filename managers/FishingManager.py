class FishingManager:

    def __init__(self, fishing_list):
        self.fishing_list = fishing_list

    def sort_fishing_list_by_price(self, reverse):
        return sorted(self.fishing_list, key=lambda fishing: fishing.price, reverse=reverse)

    def sort_fishing_list_by_name(self, reverse):
        return sorted(self.fishing_list, key=lambda fishing: fishing.name, reverse=reverse)

    def sort_fishing_list_by_season(self, reverse):
        return sorted(self.fishing_list, key=lambda fishing: fishing.season.value, reverse=reverse)

    def search_by_price(self, price):
        return list(filter(lambda fishing: fishing.price == price, self.fishing_list))

    def search_by_season(self, season):
        return list(filter(lambda fishing: fishing.season == season, self.fishing_list))