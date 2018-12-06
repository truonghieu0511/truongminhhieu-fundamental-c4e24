inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}
#1.1 +1.2
inventory["pocket"] = ["seashell", "strange berry", "lint"]
#1.3
del (inventory["backpack"][1])
#1.4
inventory["gold"] += 50
print(inventory)