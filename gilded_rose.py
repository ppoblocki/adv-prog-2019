# -*- coding: utf-8 -*-
from helper import itemIsNamed, isUnderHighestQualityValue, itemHasNonZeroValue


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if not itemIsNamed(item, "Aged Brie") and not itemIsNamed(item,"Backstage passes to a TAFKAL80ETC concert"):
                if itemHasNonZeroValue(item):
                    if itemIsNamed(item, "Conjured Mana Cake"):
                        item.quality = item.quality - 2
                    elif not itemIsNamed(item, "Sulfuras, Hand of Ragnaros"):
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if itemIsNamed(item, "Backstage passes to a TAFKAL80ETC concert"):
                        if item.sell_in < 6 and item.quality < 50:
                            item.quality += 1
                        if item.sell_in < 11:
                            if isUnderHighestQualityValue(item):
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if isUnderHighestQualityValue(item):
                                item.quality = item.quality + 1
            if not itemIsNamed(item, "Sulfuras, Hand of Ragnaros"):
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not itemIsNamed(item, "Aged Brie"):
                    if not itemIsNamed(item, "Backstage passes to a TAFKAL80ETC concert"):
                        if item.quality > 0:
                            if not itemIsNamed(item, "Sulfuras, Hand of Ragnaros"):
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
