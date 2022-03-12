import pygame
from comet import Comet

# Creer une class pour gérer cet evenement
class CometFallEvent :

    # Lors du chargement -> créer un compteur
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 20
        self.game = game
        self.fall_mode = False # gerer le mode meteore

        # Definir un groupe de sprites pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()



    def add_percent(self):
        self.percent += self.percent_speed / 100


    def is_full_loaded(self):
        return self.percent >= 100


    def reset_percent(self):
        self.percent = 0


    def meteor_fall(self):
        # Apparaitre les boules de feu
        for i in range(1,10):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # La jauge d'evenement est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True # Activer l'evenement



    def update_bar(self,surface):

        # Ajouter du poucentage à la barre
        self.add_percent()

        # Barre noir (arrière plan)
        pygame.draw.rect(surface,(0,0,0),[
            0, # Axe x
            surface.get_height() - 20, # Axe y
            surface.get_width(), # Longueur de la fenetre
            20 # epaisseur de la barre
        ])
        # Barre rouge (Jauge d'événement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # Axe x
            surface.get_height() - 20,  # Axe y
            (surface.get_width() / 100) * self.percent,  # Longueur de la fenetre
            20 # epaisseur de la barre
        ])