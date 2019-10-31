# -*- coding: utf-8 -*-
from helper import itemIsNamed, isUnderHighestQualityValue, itemHasNonZeroValue


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Quality
            if not itemIsNamed(item, "Aged Brie") and not itemIsNamed(item,"Backstage passes to a TAFKAL80ETC concert"):
                if itemHasNonZeroValue(item):
                    if item.isItemConjured():
                        item.decreaseQualityBy(2)
                    elif not item.isItemSulfuras():
                        item.decreaseQualityBy(1)
            else:
                if isUnderHighestQualityValue(item):
                    item.incrementQuality()
                    if itemIsNamed(item, "Backstage passes to a TAFKAL80ETC concert"):
                        if item.sell_in < 11 and isUnderHighestQualityValue(item):
                                item.incrementQuality()
                        if item.sell_in < 6 and isUnderHighestQualityValue(item):
                                item.incrementQuality()
            # Sell in
            if not itemIsNamed(item, "Sulfuras, Hand of Ragnaros"):
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not itemIsNamed(item, "Aged Brie"):
                    if not itemIsNamed(item, "Backstage passes to a TAFKAL80ETC concert"):
                        if itemHasNonZeroValue(item) and not itemIsNamed(item, "Sulfuras, Hand of Ragnaros"):
                                item.decreaseQualityBy(1)
                    else:
                        item.decreaseQualityBy(item.quality)
                else:
                    if isUnderHighestQualityValue(item):
                        item.incrementQuality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def incrementQuality(self):
        self.quality += 1

    def decreaseQualityBy(self, decrease):
        self.quality -= decrease

    def isItemConjured(self):
        return "Conjured" in self.name

    def isItemSulfuras(self):
        return "Sulfuras" in self.name
