class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


West_House = Room('West_House', 'You shall start your treasure hunt here', 'The_Iron_Work', 'Car_Shop', 'Hallway',
                  'Grocery_Store', None, None)
Hallway = Room('Hallway', 'You are now in the hallway', 'Living_Room', 'Bathroom', 'Continued_Hallway', 'West_House',
               'Attic', 'Basement')
Continued_Hallway = Room('Continued_Hallway', 'This hallway continues to many rooms including a basement and an attic',
                         'Living_Room', 'Bathroom', 'Public_Library', 'West_House', 'Attic', 'Basement')
Living_Room = Room('Living_Room', 'You are now in the Living_room', None, 'Hallway', 'Kitchen', 'Window', None, None)
Kitchen = Room('Kitchen', 'You are now in the kitchen', None, 'Hallway', 'Bedroom_2', 'Living_Room', None, None)
Bathroom = Room('Bathroom', 'You are now in the bathroom', 'Hallway', None, 'Bedroom_1', 'Window', None, None)
Bedroom_1 = Room('Bedroom_1', 'You are now in the Bedroom_1', 'Hallway', 'Closet_1', None, 'Bathroom', None, None)
Bedroom_2 = Room('Bedroom_2', 'You are now in the Bedroom_2',  'Closet_2', 'Hallway', 'Window', 'Kitchen', None, None)
Attic = Room('Attic', 'You are now in the attic',  None, None, None, None, None, 'Continued_Hallway')
Basement = Room('Basement', 'You find many treasures, but no one is in sight', None, None, None, None,
                'Continued_Hallway', None)
Closet_1 = Room('Closet_1', 'You are now in the closet that leads to a tunnel', 'Bedroom_2', None, None, None, None,
                'Tunnel')
Closet_2 = Room('Closet_2', 'You have two choices to go back or to go down', None, 'Bedroom_1', None, None, None,
                'Tunnel')
Tunnel = Room('Tunnel', 'There is something lurking in the tunnel', None, None, None, None, 'Closet_1', 'Closet_2')
School = Room('School', 'You are at the entrance of the high school', None, 'The_Iron_Work', None, None, None, None)
Grocery_Store = Room('Grocery_Store', 'Would you like to buy some grocery stores?', None, 'Gas_Station', 'West_House',
                     None, None, None)
Pharmacy = Room('Pharmacy', 'You are in the pharmacy', 'Gas_Station', None, 'Random_House', None, None, None)
Car_Shop = Room('Car_Shop', 'You are outside of the car shop to rent a car', 'West_House', 'Random_House', None,
                'Pharmacy', None, None)
The_Iron_Work = Room('The_Iron_Work', 'You are outside of the Iron Works', 'High_School', 'West_House', None, None,
                     None, None)
Public_Library = Room('Public_Library', 'You are inside the library and checking out all the Initial D Series!!!',
                      'Continued_Hallway', 'Nothing in Sight', None, 'Continued_Hallway', None, None)
Gas_Station = Room('Gas_Station', 'You are now putting gas in you vehicle and a bottle', 'Grocery_Store', 'Pharmacy',
                   'Car_Shop', None, None, None)
Train_Station = Room('Train_Station', 'You could attempt a train robbery, but it shall be hard to defeat the conductor',
                     'Nothing in sight', None, None, None, None, None),
Random_House = Room('Random_House', 'You are at a house that at one time people lives but is now destroyed because '
                    'of the weather',  'Car_Shop', None, 'Train_Station', 'Pharmacy', None, None)
High_School = Room('High_School', 'You did just miss class and the gates are now locked!!!', None, 'The_Iron_Work',
                   None, None, None, None)


class Item(object):
    def __init__(self, name, color, description, weight):
        self.name = name
        self.color = color
        self.description = description
        self.weight = weight


class Consumable(Item):
    def __init__(self, name, color, description, weight):
        super(Consumable, self).__init__(name, color, description, weight)


class Bottle(Consumable):
    def __init__(self, name, color, description, weight):
        super(Bottle, self).__init__(name, color, description, weight)


class Refreshment(Consumable):
    def __init__(self, name, color, description, weight):
        super(Refreshment, self).__init__(name, color, description, weight)


class Fish(Consumable):
    def __init__(self, name, color, description, weight):
        super(Fish, self).__init__(name, color, description, weight)


class Fruit(Consumable):
    def __init__(self, name, color, description, weight):
        super(Fruit, self).__init__(name, color, description, weight)


class Meat(Consumable):
    def __init__(self, name, color, description, weight):
        super(Meat, self).__init__(name, color, description, weight)


class Material(Item):
    def __init__(self, color, description, weight):
        super(Material, self).__init__(name, color, description, weight)


class Weapon(Item):
    def __init__(self, name, color, description, weight):
        super(Weapon, self).__init__(name, color, description, weight)


class Lantern(Weapon):
    def __int__(self, name, color, description, weight):
        super(Lantern, self).__init__(name, color, description, weight)


class Sword(Weapon):
    def __int__(self, name, color, description, weight):
        super(Sword, self).__init__(name, color, description, weight)


class Gun(Weapon):
    def __int__(self, name, color, description, weight):
        super(Gun, self).__init__(name, color, description, weight)


class Knife(Weapon):
    def __int__(self, name, color, description, weight):
        super(Knife, self).__init__(name, color, description, weight)


class Blade(Weapon):
    def __init__(self, name, color, description, weight):
        super(Blade, self).__init__(name, color, description, weight)


class Bomb(Weapon):
    def __init__(self, name, color, description, weight):
        super(Bomb, self).__init__(name, color, description, weight)
        self.name = 'Atomic Bomb'


class Rifle(Weapon):
    def __init__(self, name, color, description, weight):
        super(Rifle, self).__init__(name, color, description, weight)


class PowerSource(Item):
    def __init__(self, name, color, description, weight):
        super(PowerSource, self).__init__(name, color, description, weight)


class Battery(PowerSource):
    def __init__(self, name, color, description, weight):
        super(Battery, self).__init__(name, color, description, weight)


class Radio(PowerSource):
    def __init__(self, name, color, description, weight):
        super(Radio, self).__init__(name, color, description, weight)


class Panel(PowerSource):
    def __init__(self, name, color, description, weight):
        super(Panel, self).__init__(name, color, description, weight)
        self.name = 'Solar Panel'


class Water(PowerSource):
    def __init__(self, name, color, description, weight):
        super(Water, self).__init__(name, color, description, weight)


class Clothes(Item):
    def __init__(self, name, color, description, weight):
        super(Clothes, self).__init__(name, color, description, weight)


class Tuxedo(Clothes):
    def __init__(self, name, color, description, weight):
        super(Tuxedo, self).__init__(name, color, description, weight)


class Joggers(Clothes):
    def __init__(self, name, color, description, weight):
        super(Joggers, self).__init__(name, color, description, weight)


class Shirt(Clothes):
    def __init__(self, name, color, description, weight):
        super(Shirt, self).__init__(name, color, description, weight)


class Socks(Clothes):
    def __init__(self, name, color, description, weight):
        super(Socks, self).__init__(name, color, description, weight)


class Gloves(Clothes):
    def __init__(self, name, color, description, weight):
        super(Gloves, self).__init__(name, color, description, weight)


class Coat(Clothes):
    def __init__(self, name, color, description, weight):
        super(Coat, self).__init__(name, color, description, weight)


class Pants(Clothes):
    def __init__(self, name, color, description, weight):
        super(Pants, self).__init__(name, color, description, weight)


class Shorts(Clothes):
    def __init__(self, name, color, description, weight):
        super(Shorts, self).__init__(name, color, description, weight)


class Hat(Clothes):
    def __init__(self, name, color, description, weight):
        super(Hat, self).__init__(name, color, description, weight)


class Shoe(Clothes):
    def __init__(self, name, color, description, weight):
        super(Shoe, self).__init__(name, color, description, weight)


class Medicine(Item):
    def __init__(self, name, color, description, weight):
        super(Medicine, self).__init__(name, color, description, weight)


class Ibuprofen(Medicine):
    def __init__(self, name, color, description, weight):
        super(Ibuprofen, self).__init__(name, color, description, weight)


class Antibiotic(Medicine):
    def __init__(self, name, color, description, weight):
        super(Antibiotic, self).__init__(name, color, description, weight)


class Analgesic(Medicine):
    def __init__(self, name, color, description, weight):
        super(Analgesic, self).__init__(name, color, description, weight)


class Antiseptic(Medicine):
    def __init__(self, name, color, description, weight):
        super(Antiseptic, self).__init__(name, color, description, weight)


class Stabilizer(Medicine):
    def __init__(self, name, color, description, weight):
        super(Stabilizer, self).__init__(name, color, description, weight)
        self.name = 'Mood Stabilizer'


class Antipyretic(Medicine):
    def __init__(self, name, color, description, weight):
        super(Antipyretic, self).__init__(name, color, description, weight)


class Viral(Medicine):
    def __init__(self, name, color, description, weight):
        super(Viral, self).__init__(name, color, description, weight)
        self.name = 'Anti Viral'


class Fungal(Medicine):
    def __init__(self, name, color, description, weight):
        super(Fungal, self).__init__(name, color, description, weight)
        self.name = 'Anti Fungal'


class Decongestant(Medicine):
    def __init__(self, name, color, description, weight):
        super(Decongestant, self).__init__(name, color, description, weight)


class Hormone(Medicine):
    def __init__(self, name, color, description, weight):
        super(Hormone, self).__init__(name, color, description, weight)


class Vitamin(Medicine):
    def __init__(self, name, color, description, weight):
        super(Vitamin, self).__init__(name, color, description, weight)


class Stimulant(Medicine):
    def __init__(self, name, color, description, weight):
        super(Stimulant, self).__init__(name, color, description, weight)


class Opioid(Medicine):
    def __init__(self, name, color, description, weight):
        super(Opioid, self).__init__(name, color, description, weight)


input1 = {Bottle, Fish, Fruit, Fungal, Knife, Ibuprofen, Hormone, Stabilizer,
          Stimulant, Shirt, Shoe, Shorts, Panel, Pants, Sword, Gloves, Gun,
          Rifle, Blade, Antibiotic, Opioid, Vitamin, Decongestant, Antipyretic,
          Antiseptic, Analgesic, Hat, Medicine, Tuxedo, Socks, Water, Joggers,
          Radio, Lantern, Rifle, Bomb, Meat, Material, Refreshment}


class Character(object):
    def __init__(self, name, description, dialogue, health, action, death):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.health = health
        self.action = action
        self.death = death

    def death(self):
        self.death = True
        print("%s has died." % self.name)

    def damage(self, amount):
        self.health = amount
        if self.health <= 0:
            self.health = True


class Fujiwara(Character):
    def __init__(self, name, description, dialogue, health, action, death):
        super(Fujiwara, self).__init__(name, description, dialogue, health, action, death)
        self.name = 'Fujiwara'
        self.description = description
        self.dialogue = dialogue
        self.health = 100
        self.action = action
        self.death = death


input2 = [Fujiwara]
fujiwara = Fujiwara('Fujiwara', False, False, 100, False, False)


class KataGirl(Character):
    def __init__(self, name, description, dialogue, health, action, death):
        super(KataGirl, self).__init__(name, description, dialogue, health, action, death)
        self.name = 'Katagirl'
        self.description = description
        self.dialogue = dialogue
        self.health = 100
        self.action = action
        self.death = death


class Takahashi(Character):
    def __init__(self, name, description, dialogue, health, action, death):
        super(Takahashi, self).__init__(name, description, dialogue, health, action, death)
        self.name = 'Takahashi'
        self.description = description
        self.dialogue = dialogue
        self.health = 100
        self.action = action
        self.death = death


class Akio(Character):
    def __init__(self, name, description, dialogue, health, action, death):
        super(Akio, self).__init__(name, description, dialogue, health, action, death)
        self.name = 'Akio'
        self.description = description
        self.dialogue = dialogue
        self.health = 100
        self.action = action


class Ren(Character):
    def __init__(self, name, description, dialogue, health, action, death):
        super(Ren, self).__init__(name, description, dialogue, health, action, death)
        self.name = 'Ren'
        self.description = description
        self.dialogue = dialogue
        self.health = 100
        self.action = action


current_node = West_House
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
