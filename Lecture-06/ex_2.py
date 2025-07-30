inventory = [
    ["apple", 50, 0.75],
    ["banana", 100, 0.50], 
    ["orange", 75, 0.80],
]
def update_inventory(item_name, inventory, quantity_sold):
    for i in range(len(inventory)):
        if inventory[i][0] == item_name:
            inventory[i][1] += quantity_sold
            inventory[i][2] = inventory
            return
    inventory.append([item_name, quantity_sold, inventory])