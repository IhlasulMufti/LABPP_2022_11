from heroCoba import Warrior, Assassin, Support

warrior = Warrior("Manca", pos_x=10)
assassin = Assassin("Grit", pos_x=25)
support = Support("Odi", pos_x=30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

