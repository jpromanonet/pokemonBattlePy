import pygame
from functools import partial
from Button import Button

class Menu:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.rect = pygame.rect(0, 400, 160*4, 144*4)
        self.state = 0
        self.mainButtons = [
            Button(160*2, 400, 150, 40, "Luchar", partial(self.change_menu_state, newState=1)),
            Button(160*2, 450, 150, 40, "Pokemon", partial(self.change_menu_state, newState=2)),
            Button(160*3, 400, 150, 40, "Mochila", partial(self.change_menu_state, newState=3)),
            Button(160*3, 450, 150, 40, "Huir", partial(self.change_menu_state, newState=4))
        ]
        self.attackButtons = []

    def handle_event(self, event, game):
        for button in self.mainButtons:
            button.handle_event(event, game)
        if self,state == 1:
            if len(self.attackButtons) == 0:
                for idx, attack in enumerate(game.pokemon1.attacks):
                    functionTurn = partial(game.makeTurn, index=idx)
                    self.attackButtons.append(
                        Button(idx*160, 400, 150, 40, attack.name, functionTurn)
                    )
                for button in self.attackButtons:
                    button.handle_event(event, game)
        
    