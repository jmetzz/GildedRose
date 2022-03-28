# Gilded Rose Pair Programming Technical Test
Hi and welcome to team Gilded Rose! We are a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison.
We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. 
We have an inventory system in place, it takes care of updating our inventory on a daily basis for us. And, as our new Senior Developer you will be in charge of maintaining and extending it.  

## Requirements
We're planning on expanding our business and offering many new categories of items in the future and we'd like you to update our system to make it easier to maintain and support new item categories.
As the first stage of our expansion we're planning on selling a new category of **Conjured** items (they have the word "conjured" in the name).
Your task is to:
- **Update our system to support `Conjured` items**.
- **Make any improvements to the existing code you deem necessary to support our expansion**.  

## System Rules and Constraints
Our inventory system has the following main rules:
- All items have a `sell_in` value which denotes the number of days we have left to sell the item (akin to a countdown to a "sell by" date).
- All items have a `quality` value which denotes how valuable the item is.
- **At the end of each day the system lowers both `sell_in` and `quality` for every item**.  

Some items have special rules that apply only to them. Here are some of them that have been provided by from our helpful Product Manager:
- Once the sell by date has passed, `quality` degrades twice as fast.
- The `quality` of an item is never negative.
- **"Aged Brie"** actually increases in `quality` the older it gets.
- The `quality` of an item is never more than `50`.
- **"Sulfuras"**, being a legendary item, never has to be sold, nor does it decrease in `Quality`.  

This new category of item we plan on selling also has its own special rule:
- **Conjured** items degrade in `quality` twice as fast as normal items.  

Due to shortsightedness we can't modify the `Item` class or any of its properties. As its shared with other internal systems and we need to maintain interoperability with them.
Feel free to make any changes to the `GildedRose` class and add any new code as long as everything still works correctly.
