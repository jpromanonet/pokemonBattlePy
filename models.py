# Este archivo tiene las clases que modelan a nuestros pokemon que van a pelear entre si
class Battle:

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0

    def is_finished(self):
        return self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0

class Pokemon:
    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = [ ] # Con el hashtag ponemos comentarios y los arrays se definen con corchetes igual que en JS
        self.stats = {} # con las llaves definimos tuplas
        self.current_status = 0
        self.current_hp = 0

class Attack:

    def __init__(self, name, t, category, pp, power, accuracy):
        self.name = name
        self.type = t
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy

class Turn:

    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):
        return self.command1

class Command:
    def __init__(self, action):
        self.action = action