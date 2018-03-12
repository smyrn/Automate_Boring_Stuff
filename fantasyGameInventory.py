def displayInventory(inventoryDisp):
    print('Inventory:')
    item_total = 0
    for k, v in inventoryDisp.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(currInventory, addedItems):
    for item in addedItems:
        currInventory.setdefault(item, 0)
        currInventory[item] += 1
    return currInventory

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'tesla', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
