from flask import url_for


class BaseItem:
    def __init__(self, id):
        self.id = id

class HealthPotion(BaseItem):

    def __init__(self, id, size):
        super().__init__(id)
        self.size = size

    icon = 'hp_potion.png'

    def use(self, character):
        character.health += self.size
        self.size = 0