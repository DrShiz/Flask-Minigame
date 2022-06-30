from threading import Lock


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

class Knight_player(metaclass=SingletonMeta_player):
    def __init__(self):
        self.health = 150
        self.strength = 10
        self.max_health = 150
        self.max_strength = 10

    def __str__(self):
        return 'knight'

class Magician_player(metaclass=SingletonMeta_player):
    def __init__(self):
        self.health = 70
        self.strength = 25
        self.max_health = 70
        self.max_strength = 25

    def __str__(self):
        return 'magician'

class Archer_player(metaclass=SingletonMeta_player):
    def __init__(self):
        self.health = 100
        self.strength = 15
        self.max_health = 100
        self.max_strength = 15

    def __str__(self):
        return 'archer'


class Knight_enemy(metaclass=SingletonMeta_enemy):
    def __init__(self):
        self.health = 150
        self.strength = 10
        self.max_health = 150
        self.max_strength = 10

    def __str__(self):
        return 'knight'

class Magician_enemy(metaclass=SingletonMeta_enemy):
    def __init__(self):
        self.health = 70
        self.strength = 25
        self.max_health = 70
        self.max_strength = 25

    def __str__(self):
        return 'magician'

class Archer_enemy(metaclass=SingletonMeta_enemy):
    def __init__(self):
        self.health = 100
        self.strength = 15
        self.max_health = 100
        self.max_strength = 15

    def __str__(self):
        return 'archer'
