'''
Created on Nov 17, 2018

@author: domje

Hero's Inventory, with lists and dictionaries

'''
def listInventory(inventory):
    print("You have " + str(len(inventory)) + " items.")
    print("Your items: ")
    for item in inventory:
        print(item)

inventory = ["sword", "armor", "shield", "healing potion"]
listInventory(inventory) 
    
if "healing potion" in inventory:
    print("You will live to fight another day.")
    
chest = ["gold", "gems"]
print("You discover a chest and add the items to your inventory.")
inventory += chest
listInventory(inventory) 
    
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
listInventory(inventory) 
    
print("Your shield is destroyed in battle.")
del inventory[2]
listInventory(inventory) 

print("You drink your healing potion.")
drank = "healing potion"
if drank in inventory:
    inventory.remove(drank)
listInventory(inventory) 

print("You alphabateize your items for some reason.")
inventory.sort()
listInventory(inventory)

inventoryDict = {
    "sword": "A weapon used by sticking the pointy end in your enemies."
    , "armor": "Metal suit used to prevent injuries."
    , "shield": "Metal disc used to deflect sword attacks."
    , "healing potion": "Red liquid that restores 10 HP."
    , "crossbow": "Projectile weapon that shoots bolts."
    , "gold": "Coins of the realm."
    , "gems": "Diamonds, emeralds, and rubies."
    }
inventoryDict["halberd"] = "A HUUGE sword."

print(inventoryDict["healing potion"])
if "sword" in inventoryDict:
    print("We have a definition of a sword.")
print(inventoryDict.get("halberd", "Sorry, there's no definition of a halberd."))
