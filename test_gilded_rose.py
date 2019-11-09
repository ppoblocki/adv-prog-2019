# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item
from helper import item_is_named, is_under_highest_quality_value, item_has_non_zero_value, \
    left_10_days_before_dropdown, left_5_days_before_dropdown

class GildedRoseTest(unittest.TestCase):

    # Tests for helper.py
    def test_item_is_named(self):
        item = Item("Foo", 1, 1)
        self.assertTrue(item_is_named(item, "Foo"))

    def test_item_has_non_zero_value(self):
        item = Item("Bar", 1, 1)
        self.assertTrue(item_has_non_zero_value(item))

    def test_is_under_highest_quality_value(self):
        item = Item("Foo", 1, 51)
        self.assertFalse(is_under_highest_quality_value(item))

    def test_left_10_days_before_dropdown(self):
        item = Item("Bar", 10, 1)
        self.assertTrue(left_10_days_before_dropdown(item))

    def test_left_5_days_before_dropdown(self):
        item = Item("Foo", 6, 1)
        self.assertFalse(left_5_days_before_dropdown(item))

    # Gilded Rose tests
    def test_is_standard_item(self):
        item = Item("Bar", 6, 1)
        self.assertTrue(item.is_standard_item())

    def test_is_standard_item_2(self):
        unique_items = [Item("Sulfuras, Hand of Ragnaros", 1, 1), Item("Conjured Mana Cake", 2, 2),
                        Item("Backstage passes to a TAFKAL80ETC concert", 3, 3), Item("Aged Brie", 4, 4)]
        for item in unique_items:
            if item.is_standard_item():
                self.fail()

    def test_increment_quality(self):
        item = Item("Foo", 1, 1)
        item.increment_quality()
        item_2 = Item("Bar", 1, 50)
        item_2.increment_quality()
        quality_count = item.quality + item_2.quality
        self.assertEqual(quality_count, 52)

    def test_increment_and_decrease_quality_by(self):
        item = Item("Foo", 5, 45)
        item.increment_quality_by(5)
        item.decrease_quality_by(5)
        self.assertEqual(item.quality, 45)

    def test_updateQualityForStandardItem(self):
        items = [Item("Item1", 1, 1), Item("Item2", 1, 2), Item("Item3", 1, 3)]
        quality_count = 0
        for item in items:
            item.update_quality_for_standard_item()
            quality_count += item.quality
        self.assertEqual(quality_count, 3)

    def test_backstage_passes_quality_dropdown_and_increment(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)
        item.backstage_passes_quality_dropdown()
        item.backstage_passes_increment_quality()
        self.assertEqual(item.quality, 23)

    def test_update_quality_for_non_standard_item(self):
        cake = Item("Conjured Mana Cake", 2, 2)
        cake.update_quality_for_non_standard_item()
        backstage = Item("Backstage passes to a TAFKAL80ETC concert", 5, 15)
        backstage.update_quality_for_non_standard_item()
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 50, 50)
        sulfuras.update_quality_for_non_standard_item()
        quality = cake.quality + backstage.quality + sulfuras.quality
        self.assertEqual(quality, 68)

    def test_updateSellIn(self):
        item = Item("Sulfuras, Hand of Ragnaros", 50, 50)
        item_2 = Item("Aged Brie", 5, 5)
        item.updateSellIn()
        item_2.updateSellIn()
        sell_in = item.sell_in + item_2.sell_in
        self.assertEqual(sell_in, 54)


if __name__ == '__main__':
    unittest.main()
