import pygame
from functools import partial
from pygame.locals import *
from constants import *
from models.Battle import *
from models.Pokemon import *
from models.Button import *
from models.Menu import Menu
from models.GUI import GUI
import json

class Game:
    def __init__(self):
        self.buttons = []
        self.menu = Menu()
        self.gui = GUI()
        self.bg = None
        pygame.init()

        self.screen = pygame.display.set_mode(160*4, 144*4)
        pygame.display.set_caption("Sumate a Nucba =)")

        clock = pygame.time.Clock()
        clock.tick(60)

        self.initPokemonStats()
        # Attacks
        # Button(500, 500, 100, 40, 'Attack', self.makeTurn)
        self.pokemon1.attacks = [
            Attack("Cabezazo", 11, PHYSICAL, 10, 90, 100),
            Attack("Hidrobomba", 10, SPECIAL, 10, 110, 100)
        ]
        self.pokemon2.attacks = [
            Attack("Ala de Acero", 10, PHYSICAL, 10, 85, 100)
        ]
        self.loadResources()
        print('Resources loaded succesfully')
        # Start battle
        self.battle = Battle(self.pokemon1, self.pokemon2)

        self.stopped = False
        print('Initialization finished')

    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.stopped = True
            for button in self.buttons:
                button.handle_event(event, self)
            self.menu.handle_event(event, self)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print(event.pos)
    
    def loadResources(self):
        self.loadPokemonImage(self.pokemon1, True)
        self.loadPokemonImage(self.pokemon2, False)
        self.gui.loadResources()

    def loadPokemonImage(self, pokemon, isPlayer):
        pokemon_name = pokemon.name.lower()
        if isPlayer:
            pokemon_img = pygame.image.load('res/pokemon/' + pokemon_name + "_back.png")
            pokemon_img = pygame.transform.scale(pokemon_name, (300, 300))
            pokemon.renderer = pokemon_img
        else:
            pokemon_img = pygame.image.load('res/pokemon' + pokemon_name + ".png")
            pokemon_img = pygame.transform.scale(pokemon_img, (200, 300))

            pokemon.renderer = pokemon_img

        self.bg = pygame.image.load('res/battle_bg/battle_bg_1.png')
        self.bg = pygame.transform.scale(self.bg, (160*4, 400))

    def initPokemonStats(self):
        # First define pokemons with its stats

        pokemon1 = "Blastoise"
        pokemon2 = "Skarmony"
        with open('db/pokemons.json') as f:
            data = json.load(f)
            type2 = None
            if "type2" in data[pokemon1].keys():
                type2 = data[pokemon1]["type2"]
            self.pokemon1 = Pokemon(pokemon1, 100, data[pokemon1]["type1"], type2)
            type22 = None
            if "type2" in data[pokemon2]:
                type22 = data[pokemon2]["type2"]
            self.pokemon2 = Pokemon(pokemon2, 100, data[pokemon2]["type1"], type22)
            self.pokemon1.baseStats = {
                HP: data[self.pokemon1.name]["HP"]
            }