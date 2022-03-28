# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_sell_in(self):        
        item = Item("foo", 10, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(9, item.sell_in)        

    def test_quality_zero(self):
        item = Item("foo", 0, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(0, item.quality)

    def test_quality_decreases_by_one(self):
        item = Item("foo", 10, 5)
        expected = item.quality-1
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(expected, item.quality)

    def test_quality_decreases_by_two(self):
        item = Item("foo", 0, 5)
        expected = item.quality-2
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(expected, item.quality)

    def test_aged_brie_increases_in_quality(self):
        item = Item("Aged Brie", 20, 5)
        expected = item.quality+1
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(expected, item.quality)

    def test_aged_brie_increases_in_quality_but_never_more_than_50(self):
        item = Item("Aged Brie", 20, 50)
        expected = item.quality
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(expected, item.quality)

    def test_sulfuras_never_changes_quality(self):
        item = Item("Sulfuras, Hand of Ragnaros", 20, 5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(5, item.quality)

    def test_sulfuras_never_changes_sell_in(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(5, item.sell_in)        

if __name__ == '__main__':
    unittest.main()
