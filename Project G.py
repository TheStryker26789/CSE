class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, item):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


West_House = Room('West_House', 'You shall start your treasure hunt here', 'The_Iron_Work', 'Car_Shop', 'Hallway',
                  'Grocery_Store', None, None, 'GT86')
Hallway = Room('Hallway', 'You are now in the hallway', 'Living_Room', 'Bathroom', 'Continued_Hallway', 'West_House',
               'Attic', 'Basement', None)
Continued_Hallway = Room('Continued_Hallway', 'This hallway continues to many rooms including a basement and an attic',
                         'Living_Room', 'Bathroom', 'Public_Library', 'West_House', 'Attic', 'Basement', None)
Living_Room = Room('Living_Room', 'You are now in the Living_room', None, 'Hallway', 'Kitchen', 'Window', None, None,
                   'MX5')
Kitchen = Room('Kitchen', 'You are now in the kitchen', None, 'Hallway', 'Bedroom_2', 'Living_Room', None, None, None)
Bathroom = Room('Bathroom', 'You are now in the bathroom', 'Hallway', None, 'Bedroom_1', 'Window', None, None, None)
Bedroom_1 = Room('Bedroom_1', 'You are now in the Bedroom_1', 'Hallway', 'Closet_1', None, 'Bathroom', None, None, None)
Bedroom_2 = Room('Bedroom_2', 'You are now in the Bedroom_2',  'Closet_2', 'Hallway', 'Window', 'Kitchen', None, None,
                 None)
Attic = Room('Attic', 'You are now in the attic',  None, None, None, None, None, 'Continued_Hallway', 'R33')
Basement = Room('Basement', 'You find many treasures, but no one is in sight', None, None, None, None,
                'Continued_Hallway', None, 'R34')
Closet_1 = Room('Closet_1', 'You are now in the closet that leads to a tunnel', 'Bedroom_2', None, None, None, None,
                'Tunnel', None)
Closet_2 = Room('Closet_2', 'You have two choices to go back or to go down', None, 'Bedroom_1', None, None, None,
                'Tunnel', None)
Tunnel = Room('Tunnel', 'There is something lurking in the tunnel', None, None, None, None, 'Closet_1', 'Closet_2',
              None)
School = Room('School', 'You are at the entrance of the high school', None, 'The_Iron_Work', None, None, None, None,
              'Integra')
Grocery_Store = Room('Grocery_Store', 'Would you like to buy some grocery stores?', None, 'Gas_Station', 'West_House',
                     None, None, None, 'R32')
Pharmacy = Room('Pharmacy', 'You are in the pharmacy', 'Gas_Station', None, 'Random_House', None, None, None,
                'Evolution')
Car_Shop = Room('Car_Shop', 'You are outside of the car shop to rent a car', 'West_House', 'Random_House', None,
                'Pharmacy', None, None, 'Impreza')
The_Iron_Work = Room('The_Iron_Work', 'You are outside of the Iron Works', 'High_School', 'West_House', None, None,
                     None, None, 'S2000')
Public_Library = Room('Public_Library', 'You are inside the library and checking out all the Initial D Series!!!',
                      'Continued_Hallway', 'Nothing in Sight', None, 'Continued_Hallway', None, None, 'AE86')
Gas_Station = Room('Gas_Station', 'You are now putting gas in you vehicle and a bottle', 'Grocery_Store', 'Pharmacy',
                   'Car_Shop', None, None, None, 'FD')
Train_Station = Room('Train_Station', 'You could attempt a train robbery, but it shall be hard to defeat the conductor',
                     'Nothing in sight', None, None, None, None, None, 'S15'),
Random_House = Room('Random_House', 'You are at a house that at one time people lives but is now destroyed because '
                    'of the weather',  'Car_Shop', None, 'Train_Station', 'Pharmacy', None, None, 'FC')
High_School = Room('High_School', 'You did just miss class and the gates are now locked!!!', None, 'The_Iron_Work',
                   None, None, None, None, 'Supra')


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


class Movie(Item):
    def __init__(self, name, color, description, weight):
        super(Movie, self).__init__(name, color, description, weight)


class InitialD(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialD, self).__init__(name, color, description, weight)
        self.name = 'Initial d'


class InitialD2ndStage(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialD2ndStage, self).__init__(name, color, description, weight)
        self.name = 'Initial D 2nd Stage'


class InitialD3rdStage(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialD3rdStage, self).__init__(name, color, description, weight)
        self.name = 'Initial D 3rd Stage'


class InitialD4thStage(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialD4thStage, self).__init__(name, color, description, weight)
        self.name = 'Initial D 4th Stage'


class InitialD5thStage(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialD5thStage, self).__init__(name, color, description, weight)
        self.name = 'Initial D 5th Stage'


class InitialDFinalStage(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDFinalStage, self).__init__(name, color, description, weight)
        self.name = 'Initial D Final Stage'


class InitialDLEGEND1(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDLEGEND1, self).__init__(name, color, description, weight)
        self.name = 'Initial D Legend 1'


class InitialDLegend2(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDLegend2, self).__init__(name, color, description, weight)
        self.name = 'Initial D Legend 2'


class InitialDLegend3(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDLegend3, self).__init__(name, color, description, weight)
        self.name = 'Initial D Legend 3'


class InitialDBattleStage(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDBattleStage, self).__init__(name, color, description, weight)
        self.name = 'Initial D Battle Stage'


class InitialDBattleStage2(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDBattleStage2, self).__init__(name, color, description, weight)
        self.name = 'Initial D Battle Stage 2'


class InitialDExtraStage(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDExtraStage, self).__init__(name, color, description, weight)
        self.name = 'Initial D Extra Stage'


class InitialDExtraStage2(Movie):
    def __init__(self, name, color, description, weight):
        super(InitialDExtraStage2, self).__init__(name, color, description, weight)
        self.name = 'Initial D Extra Stage 2'


class Car(Item):
    def __init__(self, name, color, description, weight):
        super(Car, self).__init__(name, color, description, weight)


class AE86(Car):
    def __init__(self, name, color, description, weight):
        super(AE86, self).__init__(name, color, description, weight)
        self.name = 'Toyota Sprinter Trueno'
        self.chassis = 'AE86'
        self.aspiration = natural
        self.hp = 240
        self.torque = 200
        self.style = hatchback
        self.doors = 3
        self.weight = 2200


class GT86(Car):
    def __init__(self, name, color, description, weight):
        super(GT86, self).__init__(name, color, description, weight)
        self.name = 'Toyota 86'
        self.chassis = 'GT86'
        self.aspiration = natural
        self.hp = 205
        self.torque = 155
        self.style = coupe
        self.doors = 2
        self.weight = 2800


class Supra(Car):
    def __init__(self, name, color, description, weight):
        super(Supra, self).__init__(name, color, description, weight)
        self.name = 'Toyota Supra Turbo'
        self.chassis = 'A80'
        self.aspiration = turbocharged
        self.hp = 320
        self.torque = 315
        self.style = hatchback
        self.doors = 3
        self.weight = 3400


class MR2(Car):
    def __init__(self, name, color, description, weight):
        super(MR2, self).__init__(name, color, description, weight)
        self.name = 'Toyota MR-2'
        self.chassis = 'AW11'
        self.aspiration = supercharged
        self.hp = 170
        self.torque = 155
        self.style = Coupe
        self.doors = 2
        self.weight = 2500


class MX5(Car):
    def __init__(self, name, color, description, weight):
        super(MX5, self).__init__(name, color, description, weight)
        self.name = 'Mazda Miata'
        self.chassis = 'NA'
        self.aspiration = natural
        self.hp = 130
        self.torque = 110
        self.style = convertible
        self.doors = 2
        self.weight = 2100


class FD(Car):
    def __init__(self, name, color, description, weight):
        super(FD, self).__init__(name, color, description, weight)
        self.name = 'Mazda Rx7'
        self.chassis = 'FD'
        self.aspiration = twin_turbo
        self.hp = 300
        self.torque = 260
        self.style = hatchback
        self.doors = 3
        self.weight = 2900


class FC(Car):
    def __init__(self, name, color, description, weight):
        super(FC, self).__init__(name,  color, description, weight)
        self.name = 'Mazda Rx7'
        self.chassis = 'FC'
        self.aspiration = turbocharged
        self.hp = 260
        self.torque = 220
        self.style = hatchback
        self.doors = 3
        self.weight = 2800


class R34(Car):
    def __init__(self, name, color, description, weight):
        super(R34, self).__init__(name, color, description, weight)
        self.name = 'Nissan Skyline GT-R'
        self.chassis = 'GF-BNR34'
        self.aspiration = turbocharged
        self.hp = 500
        self.torque = 540
        self.style = coupe
        self.doors = 2
        self.weight = 3300


class R33(Car):
    def __init__(self, name, color, description, weight):
        super(R33, self).__init__(name,  color, description, weight)
        self.name = 'Nissan Skyline GT-R'
        self.chassis = 'E-BCNR33'
        self.aspiration = turbocharged
        self.hp = 400
        self.torque = 350
        self.style = coupe
        self.doors = 2
        self.weight = 3400


class R32(Car):
    def __init__(self, name, color, description, weight):
        super(R32, self).__init__(name, color, description, weight)
        self.name = 'Nissan Skyline GT-R'
        self.chassis = 'E-BNR32'
        self.aspiration = turbocharged
        self.hp = 600
        self.torque = 550
        self.style = coupe
        self.doors = 2
        self.weight = 2600


class S15(Car):
    def __init__(self, name, color, description, weight):
        super(S15, self).__init__(name, color, description, weight)
        self.name = 'Nissan Silvia'
        self.chassis = 'S'
        self.aspiration = turbocharged
        self.hp = 270
        self.torque = 220
        self.style = coupe
        self.doors = 2
        self.weight = 2700


class S2000(Car):
    def __init__(self, name, color, description, weight):
        super(S2000, self).__init__(name, color, description, weight)
        self.name = 'Honda S2000'
        self.chassis = 'AP1'
        self.aspiration = natural
        self.hp = 240
        self.torque = 151
        self.style = convertible
        self.doors = 2
        self.weight = 2800


class Integra(Car):
    def __init__(self, name, color, description, weight):
        super(Integra, self).__init__(name, color, description, weight)
        self.name = 'Honda Integra Type R'
        self.chassis = 'DC2'
        self.aspiration = natural
        self.hp = 200
        self.torque = 137
        self.style = Coupe
        self.doors = 2
        self.weight = 2600


class Civic(Car):
    def __init__(self, name, color, description, weight):
        super(Civic, self).__init__(name, color, description, weight)
        self.name = 'Honda Civic Type R'
        self.chassis = 'EK9'
        self.aspiration = natural
        self.hp = 190
        self.torque = 120
        self.style = hatchback
        self.doors = 3
        self.weight = 2400


class Impreza(Car):
    def __init__(self, name, color, description, weight):
        super(Impreza, self).__init__(name, color, description, weight)
        self.name = 'Subaru Impreza WRX STI 22b'
        self.chassis = 'GC8E'
        self.aspiration = turbo
        self.hp = 350
        self.torque = 305
        self.style = coupe
        self.doors = 2
        self.weight = 2800


class Evolution(Car):
    def __init__(self, name, color, description, weight):
        super(Evolution, self).__init__(name, color, description, weight)
        self.name = 'Mitsubishi Lancer Evolution'
        self.chassis = 'CT9A'
        self.aspiration = turbo
        self.hp = 405
        self.torque = 350
        self.style = sedan
        self.doors = 4
        self.weight = 2700


class Engine(Item):
    def __init__(self, name, color, description, weight):
        super(Engine, self).__init__(name, color, description, weight)


class A(Engine):
    def __init__(self, name, color, description, weight):
        super(A, self).__init__(name, color, description, weight)
        self.name = '4age'
        self.cylinder = 4
        self.hp = 150
        self.rev_limit = 7500
        self.liters = 1.6
        self.valve = 16


class TRDGroupA(Engine):
    def __init__(self, name, color, description, weight):
        super(TRDGroupA, self).__init__(name, color, description, weight)
        self.name = '4ag'
        self.cylinder = 4
        self.hp = 240
        self.rev_limit = 11000
        self.liters = 1.6
        self.valve = 20


class LRGUE(Engine):
    def __init__(self, name, color, description, weight):
        super(LRGUE, self).__init__(name, color, description, weight)
        self.name = '1LR-GUE'
        self.cylinder = 10
        self.hp = 560
        self.rev_limit = 9500
        self.liters = 4.8
        self.valve = 40


class Rotary(Engine):
    def __init__(self, name, color, description, weight):
        super(Rotary, self).__init__(name, color, description, weight)
        self.name = 'Wankle engine'
        self.cylinder = None
        self.hp = 300
        self.rev_limit = 8000
        self.liters = 1.3
        self.valve = None


class RB(Engine):
    def __init__(self, name, color, description, weight):
        super(RB, self).__init__(name, color, description, weight)
        self.name = 'RB26'
        self.cylinder = 6
        self.hp = 330
        self.rev_limit = 8200
        self.liters = 2.6
        self.valve = 24


class RBX(Engine):
    def __init__(self, name, color, description, weight):
        super(RBX, self).__init__(name, color, description, weight)
        self.name = 'RBX-GT2'
        self.cylinder = 6
        self.hp = 400
        self.rev_limit = 8000
        self.liters = 2.8
        self.valve = 24


class SR(Engine):
    def __init__(self, name, color, description, weight):
        super(SR, self).__init__(name, color, description, weight)
        self.name = 'SR20DET'
        self.cylinder = 4
        self.hp = 210
        self.rev_limit = 7000
        self.liters = 2.0
        self.valve = 16


class JZ(Engine):
    def __init__(self, name, color, description, weight):
        super(JZ, self).__init__(name, color, description, weight)
        self.name = '2jz'
        self.cylinder = 6
        self.hp = 330
        self.rev_limit = 7200
        self.liters = 3.0
        self.valve = 24


class J(Engine):
    def __init__(self, name, color, description, weight):
        super(J, self).__init__(name, color, description, weight)
        self.name = '1JZ'
        self.cylinder = 6
        self.hp = 300
        self.rev_limit = 7000
        self.liters = 2.5
        self.valve = 24


class Yamaha(Engine):
    def __init__(self, name, color, description, weight):
        super(Yamaha, self).__init__(name, color, description, weight)
        self.name = '2ZZ'
        self.cylinder = 4
        self.hp = 190
        self.rev_limit = 8600
        self.liters = 1.8
        self.valve = 16


class ZZ(Engine):
    def __init__(self, name, color, description, weight):
        super(ZZ, self).__init__(name, color, description, weight)
        self.name = '1ZZ'
        self.cylinder = 4
        self.hp = 140
        self.rev_limit = 6400
        self.liters = 1.8
        self.valve = 16


class FA(Engine):
    def __init__(self, name, color, description, weight):
        super(FA, self).__init__(name, color, description, weight)
        self.name = 'FA20 H4'
        self.cylinder = 4
        self.hp = 205
        self.liters = 2.0
        self.valve = 16


class B(Engine):
    def __init__(self, name, color, description, weight):
        super(B, self).__init__(name, color, description, weight)
        self.name = 'B16'
        self.cylinder = 4
        self.hp = 187
        self.rev_limit = 8400
        self.liters = 1.6
        self.valve = 16


class F(Engine):
    def __init__(self, name, color, description, weight):
        super(F, self).__init__(name, color, description, weight)
        self.name = 'F20C'
        self.cylinder = 4
        self.hp = 240
        self.rev_limit = 9000
        self.liters = 2.0
        self.valve = 16


class K(Engine):
    def __init__(self, name, color, description, weight):
        super(K, self).__init__(name, color, description, weight)
        self.name = 'K20'
        self.cylinder = 4
        self.hp = 220
        self.rev_limit = 8000
        self.liters = 2.0
        self.valve = 16


class EJ(Engine):
    def __init__(self, name, color, description, weight):
        super(EJ, self).__init__(name, color, description, weight)
        self.name = 'EJ22'
        self.cylinder = 4
        self.hp = 350
        self.rev_limit = 8000
        self.liters = 2.2
        self.valve = 16


class Boxer4(Engine):
    def __init__(self, name, color, description, weight):
        super(Boxer4, self).__init__(name, color, description, weight)
        self.name = 'EJ25'
        self.cylinder = 4
        self.hp = 310
        self.rev_limit = 8000
        self.liter = 2.5
        self.valve = 16


class Sirus(Engine):
    def __init__(self, name, color, description, weight):
        super(Sirus, self).__init__(name, color, description, weight)
        self.name = '4G63'
        self.cylinder = 4
        self.hp = 300
        self.rev_limit = 8000
        self.liters = 2.0
        self.valve = 16


class Hemi(Engine):
    def __init__(self, name, color, description, weight):
        super(Hemi, self).__init__(name, color, description, weight)
        self.name = '426 Hemi'
        self.cylinder = 8
        self.hp = 425
        self.rev_limit = 5500
        self.liters = 7.0
        self.valve = 16


class SRT(Engine):
    def __init__(self, name, color, description, weight):
        super(SRT, self).__init__(name, color, description, weight)
        self.name = 'Supercharged Hemi'
        self.cylinder = 8
        self.hp = 840
        self.rev_limit = 6400
        self.liters = 6.2
        self.valve = 16


input1 = {Bottle, Fish, Fruit, Fungal, Knife, Ibuprofen, Hormone, Stabilizer,
          Stimulant, Shirt, Shoe, Shorts, Panel, Pants, Sword, Gloves, Gun,
          Rifle, Blade, Antibiotic, Opioid, Vitamin, Decongestant, Antipyretic,
          Antiseptic, Analgesic, Hat, Medicine, Tuxedo, Socks, Water, Joggers,
          Radio, Lantern, Rifle, Bomb, Meat, Material, Refreshment, Movie, Car, Engine}


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


class Mika(Character):
    def __init__(self, name, description, dialogue, health, action, death):
        super(Mika, self).__init__(name, description, dialogue, health, action, death)
        self.name = 'Mika'
        self.description = description
        self.dialogue = dialogue
        self.health = 100
        self.action = action


class Mako(Character):
    def __init__(self, name, description, dialogue, health, action, death):
        super(Mako, self).__init__(name, description, dialogue, health, action, death)
        self.name = 'Mako'
        self.description = description
        self. dialogue = dialogue
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
