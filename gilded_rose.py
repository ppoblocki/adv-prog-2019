# -*- coding: utf-8 -*-
from helper import itemIsNamed, isUnderHighestQualityValue, itemHasNonZeroValue, left10DaysBeforeDropdown, \
    left5DaysBeforeDropdown


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Quality update
            if item.isStandardItem():
                item.updateQualityForStandardItem()
            else:
                item.updateQualityForNonStandardItem()
            # Sell in update
            item.updateSellIn()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def isStandardItem(self):
        if self.name in ["Conjured Mana Cake", "Sulfuras, Hand of Ragnaros",
                         "Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
            return False
        else:
            return True

    def incrementQuality(self):
        if isUnderHighestQualityValue(self):
            self.quality += 1

    def incrementQualityBy(self, increment):
        if isUnderHighestQualityValue(self):
            self.quality += increment

    def decreaseQualityBy(self, decrease):
        if itemHasNonZeroValue(self):
            self.quality -= decrease

    def updateQualityForStandardItem(self):
        if itemHasNonZeroValue(self):
            self.quality -= 1

    def backstagePassesQualityDropdown(self):
        if self.sell_in < 0:
            self.quality = 0

    def backstagePassesIncrementQuality(self):
        self.incrementQuality()
        if left5DaysBeforeDropdown(self):
            self.incrementQualityBy(2)
        elif left10DaysBeforeDropdown(self):
            self.incrementQuality()

    def updateQualityForNonStandardItem(self):
        if itemIsNamed(self, "Conjured Mana Cake"):
            self.decreaseQualityBy(2)
        elif itemIsNamed(self, "Backstage passes to a TAFKAL80ETC concert"):
            self.backstagePassesIncrementQuality()
        else:
            self.incrementQuality()

    def updateSellIn(self):
        self.sell_in -= 1
        if itemIsNamed(self, "Sulfuras, Hand of Ragnaros"):
            self.sell_in += 1
        elif itemIsNamed(self, "Aged Brie"):
            self.incrementQuality()
        elif itemIsNamed(self, "Backstage passes to a TAFKAL80ETC concert"):
            self.backstagePassesQualityDropdown()
