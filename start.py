from modules.classes import Item, Weapon, Character
from modules.generate import generateSword

#print("josh.name: " + josh.name)
#print("josh.inventory: " + str(josh.inventory))
#print("josh.weightCap: " + str(josh.weightCap))
#print("josh.weightCur: "+ str(josh.weightCur))
#print("josh.resilience: " + str(josh.resilience))
#print("josh.strength: " + str(josh.strength))
#print("josh.dexterity: " + str(josh.dexterity))
#print("josh.accuracy: " + str(josh.accuracy))
#print("josh.equipped: " + str(josh.equipped))

josh = Character("Josh", "fighter")
josh.addItemToInventory(generateSword(160))
josh.addItemToInventory(generateSword(400))
josh.addItemToInventory(generateSword(20))

#josh.addItemToInventory(Weapon("josh sword", 10, 12, 13, 14, 15))
#josh.addItemToInventory(Weapon("josh second sword", 10, 12, 13, 14, 15))

#print("sword.name: " + sword.name)
#print("sword.weight: " + str(sword.weight))
#print("sword.value: " + str(sword.value))
#print("sword.piercing: " + str(sword.piercing))
#print("sword.slashing: " + str(sword.slashing))
#print("sword.blunt: " + str(sword.blunt))

josh.printStatus()
