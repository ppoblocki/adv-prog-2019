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

    def test_incrementAndDecreaseQualityBy(self):
        item = Item("Foo", 5, 45)
        item.incrementQualityBy(5)
        item.decreaseQualityBy(5)
        self.assertEqual(item.quality, 45)

    def test_updateQualityForStandardItem(self):
        items = [Item("Item1", 1, 1), Item("Item2", 1, 2), Item("Item3", 1, 3)]
        qualityCount = 0
        for item in items:
            item.updateQualityForStandardItem()
            qualityCount += item.quality
        self.assertEqual(qualityCount, 3)

    def test_backstagePassesQualityDropdownAndIncrement(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)
        item.backstagePassesQualityDropdown()
        item.backstagePassesIncrementQuality()
        self.assertEqual(item.quality, 23)

    def test_updateQualityForNonStandardItem(self):
        item = Item("Conjured Mana Cake", 2, 2)
        item.updateQualityForNonStandardItem()
        self.assertEqual(item.quality, 0)

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
