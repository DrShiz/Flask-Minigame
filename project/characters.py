from threading import Lock
from random import randrange


characters = ['knight', 'magician', 'archer']

class SingletonMeta_player(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonMeta_enemy(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class BaseCharacter:
    
    def roll_the_dice(self):
        return (randrange(1, 6), randrange(1, 6))

    parts = ['head', 'body', 'hands', 'legs']

class Knight_player(BaseCharacter, metaclass=SingletonMeta_player):
    def __init__(self):
        self.health = 150
        self.strength = 10
        self.max_health = 150
        self.max_strength = 10

    def __str__(self):
        return 'knight'

class Magician_player(BaseCharacter, metaclass=SingletonMeta_player):
    def __init__(self):
        self.health = 70
        self.strength = 25
        self.max_health = 70
        self.max_strength = 25

    def __str__(self):
        return 'magician'

class Archer_player(BaseCharacter, metaclass=SingletonMeta_player):
    def __init__(self):
        self.health = 100
        self.strength = 15
        self.max_health = 100
        self.max_strength = 15

    def __str__(self):
        return 'archer'


class Knight_enemy(BaseCharacter, metaclass=SingletonMeta_enemy):
    def __init__(self):
        self.health = 150
        self.strength = 10
        self.max_health = 150
        self.max_strength = 10

    def __str__(self):
        return 'knight'

class Magician_enemy(BaseCharacter, metaclass=SingletonMeta_enemy):
    def __init__(self):
        self.health = 70
        self.strength = 25
        self.max_health = 70
        self.max_strength = 25

    def __str__(self):
        return 'magician'

class Archer_enemy(BaseCharacter, metaclass=SingletonMeta_enemy):
    def __init__(self):
        self.health = 100
        self.strength = 15
        self.max_health = 100
        self.max_strength = 15

    def __str__(self):
        return 'archer'
