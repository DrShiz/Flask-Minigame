from threading import Lock
from random import randrange
from .items import HealthPotion
import json


characters = ['Knight', 'Magician', 'Archer']

class BaseCharacter:

    health = 0
    strength = 0
    max_health = 0
    max_strength = 0
    
    def roll_the_dice(self):
        self.dices = [randrange(1, 6), randrange(1, 6)]
        self.dices_sum = sum(self.dices)

    parts = {
        'Head': {
            'chance': 0.7,
            'criticality': 1
        }, 
        'Body': {
            'chance': 0.9,
            'criticality': 0.8
        }, 
        'Hands': {
            'chance': 0.4,
            'criticality': 0.3
        }, 
        'Legs': {
            'chance': 0.6,
            'criticality': 0.5
        }
    }

    inventory = {
        'items': {},
        'meta': {
            'next_itemid': 1
        }}

    def add_item_to_inventory(self, item):
        item.id = self.inventory['meta']['next_itemid']
        self.inventory['meta']['next_itemid'] += 1
        self.inventory['items'][item.id] = item


    def use_item(self, item):

        item.use(self)

    attack_target = ''


class Knight(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.health = 150
        self.strength = 10
        self.max_health = 150
        self.max_strength = 10
        hp_potion=HealthPotion(30)
        self.inventory = super().inventory
        self.attack_target = super().attack_target
        self.add_item_to_inventory(hp_potion)

    def __str__(self):
        return 'Knight'


class Magician(BaseCharacter):
    def __init__(self):
        self.health = 70
        self.strength = 25
        self.max_health = 70
        self.max_strength = 25

    def __str__(self):
        return 'Magician'

class Archer(BaseCharacter):
    def __init__(self):
        self.health = 100
        self.strength = 15
        self.max_health = 100
        self.max_strength = 15

    def __str__(self):
        return 'Archer'
