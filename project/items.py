from flask import url_for


class HealthPotion:

    def __init__(self, size):
        self.size = size

    icon = 'hp_potion.png'

    def use(self, character):
        character.health += self.size
        self.size = 0