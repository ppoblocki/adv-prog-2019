# -*- coding: utf-8 -*-
'''gilded_rose.py'''

from helper import item_is_named, is_under_highest_quality_value, item_has_non_zero_value, \
     left_10_days_before_dropdown, left_5_days_before_dropdown


class GildedRose():
    '''GildedRose class.'''
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        '''Updates item's quality and sell_in attributes.'''
        for item in self.items:
            # Quality update
            if item.is_standard_item():
                item.update_quality_for_standard_item()
            else:
                item.update_quality_for_non_standard_item()
            # Sell in update
            item.update_sell_in()


class Item:
    '''Item class.'''
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def is_standard_item(self):
        '''Checks if item is a standard item or unique.'''
        return not self.name in ["Conjured Mana Cake", "Sulfuras, Hand of Ragnaros",
                                 "Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]

    def increment_quality(self):
        '''Increments item's quality by 1.'''
        if is_under_highest_quality_value(self):
            self.quality += 1

    def increment_quality_by(self, increment):
        '''Increments item's quality by specific value.'''
        if is_under_highest_quality_value(self):
            self.quality += increment

    def decrease_quality_by(self, decrease):
        '''Decreases item's quality by specific value.'''
        if item_has_non_zero_value(self):
            self.quality -= decrease

    def update_quality_for_standard_item(self):
        '''Updates quality for standard items.'''
        if item_has_non_zero_value(self):
            self.quality -= 1

    def backstage_passes_quality_dropdown(self):
        '''Checks if backstage passes dropdown occurred.'''
        if self.sell_in < 0:
            self.quality = 0

    def backstage_passes_increment_quality(self):
        '''Increments backstage passes quality.'''
        self.increment_quality()
        if left_5_days_before_dropdown(self):
            self.increment_quality_by(2)
        elif left_10_days_before_dropdown(self):
            self.increment_quality()

    def update_quality_for_non_standard_item(self):
        '''Updates quality for non-standard items.'''
        if item_is_named(self, "Conjured Mana Cake"):
            self.decrease_quality_by(2)
        elif item_is_named(self, "Backstage passes to a TAFKAL80ETC concert"):
            self.backstage_passes_increment_quality()
        else:
            self.increment_quality()

    def update_sell_in(self):
        '''Updates sell_in attribute.'''
        self.sell_in -= 1
        if item_is_named(self, "Sulfuras, Hand of Ragnaros"):
            self.sell_in += 1
        elif item_is_named(self, "Aged Brie"):
            self.increment_quality()
        elif item_is_named(self, "Backstage passes to a TAFKAL80ETC concert"):
            self.backstage_passes_quality_dropdown()
