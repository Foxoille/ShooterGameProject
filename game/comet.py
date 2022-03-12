import pygame
import random

# Crée une class pour gérer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self,comet_event):
        super().__init__()

        # Definir l'image associée à cette comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,400)
        self.comet_event = comet_event


    def remove(self):
        self.comet_event.all_comets.remove(self)

        # Jouer le son
        self.comet_event.game.sound_menager.play('meteorite')

        # Verifier si le nombre de comettes est de 0
        if len(self.comet_event.all_comets) == 0:
            # Remettre la barre à 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers monstre
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # Ne tombe pas sur le sol
        if self.rect.y >= 500:
            # Retirer la boule de feu
            self.remove()

            # Si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("L'evenement est fini")
                # remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode= False

        # Verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print("Joueur touché")
            # Retirer la boule de feu
            self.remove()

            # Subir 20 pts de degats
            self.comet_event.game.player.damage(20)