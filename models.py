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