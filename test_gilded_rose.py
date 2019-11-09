# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item

from helper import itemIsNamed, isUnderHighestQualityValue, itemHasNonZeroValue, left10DaysBeforeDropdown, \
    left5DaysBeforeDropdown

class GildedRoseTest(unittest.TestCase):

    # Tests for helper.py
    def test_itemIsNamed(self):
        item = Item("Foo", 1, 1)
        self.assertTrue(itemIsNamed(item, "Foo"))

    def test_itemHasNonZeroValue(self):
        item = Item("Bar", 1, 1)
        self.assertTrue(itemHasNonZeroValue(item))

    def test_isUnderHighestQualityValue(self):
        item = Item("Foo", 1, 51)
        self.assertFalse(isUnderHighestQualityValue(item))

    def test_left10DaysBeforeDropdown(self):
        item = Item("Bar", 10, 1)
        self.assertTrue(left10DaysBeforeDropdown(item))

    def test_left5DaysBeforeDropdown(self):
        item = Item("Foo", 6, 1)
        self.assertFalse(left5DaysBeforeDropdown(item))

    # Glided Rose tests
    def test_isStandardItem(self):
        item = Item("Bar", 6, 1)
        self.assertTrue(item.isStandardItem())

    def test_isStandardItem_2(self):
        uniqueItems = [Item("Sulfuras, Hand of Ragnaros", 1, 1), Item("Conjured Mana Cake", 2, 2),
                       Item("Backstage passes to a TAFKAL80ETC concert", 3, 3), Item("Aged Brie", 4, 4)]
        for item in uniqueItems:
            if item.isStandardItem():
                self.fail()

    def test_incrementQuality(self):
        item = Item("Foo", 1, 1)
        item.incrementQuality()
        item2 = Item("Bar", 1, 50)
        item2.incrementQuality()
        qualityCount = item.quality + item2.quality
        self.assertEqual(qualityCount, 52)

    def test_incrementQualityBy(self):
        item = Item("Foo", 1, 1)
        item.incrementQualityBy(5)
        self.assertEqual(item.quality, 6)

    def test_decreaseQualityBy(self):
        item = Item("Bar", 1, 50)
        item.decreaseQualityBy(10)
        self.assertEqual(item.quality, 40)

    def test_updateQualityForStandardItem(self):
        item = Item("Bar", 1, 25)
        item.updateQualityForStandardItem()
        self.assertEqual(item.quality, 24)

    def test_backstagePassesQualityDropdown(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)
        item.backstagePassesQualityDropdown()
        self.assertEqual(item.quality, 20)

    def test_backstagePassesIncrementQuality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)
        item.backstagePassesIncrementQuality()
        self.assertEqual(item.quality, 23)

    def test_backstagePassesIncrementQuality_2(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 20)
        item.backstagePassesIncrementQuality()
        self.assertEqual(item.quality, 22)

    def test_updateQualityForNonStandardItem(self):
        item = Item("Conjured Mana Cake", 2, 2)
        item.updateQualityForNonStandardItem()
        self.assertEqual(item.quality, 0)

    def test_updateQualityForNonStandardItem_2(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 2)
        item.updateQualityForNonStandardItem()
        self.assertEqual(item.quality, 5)

    def test_updateSellIn(self):
        item = Item("Sulfuras, Hand of Ragnaros", 50, 50)
        item.updateSellIn()
        self.assertEqual(item.sell_in, 50)

    def test_updateSellIn_2(self):
        item = Item("Aged Brie", 5, 5)
        item.updateSellIn()
        self.assertEqual(item.sell_in, 4)


if __name__ == '__main__':
    unittest.main()
