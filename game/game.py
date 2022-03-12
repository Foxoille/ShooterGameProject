from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager
import pygame

class Game:

    def __init__(self):
        # Definir si le jeu à commencé
        self.is_playing = False

        # Gerer l'Evenement
        self.comet_event = CometFallEvent(self)

        # Groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        # Gerer les comettes
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()

        # Gerer le son
        self.sound_menager = SoundManager()

        # Gerer le score
        self.score = 0


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)


    def add_score(self, points):
        self.score += points



    def game_over(self):
        # Remettre le jeu à neuf / retirer les monstrers, remettre le joueur à 100pv et afficher le menu
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        # Jouer le son
        self.sound_menager.play('game_over')

    def update(self,screen):

        # Afficher le score
        font = pygame.font.SysFont("monospace",16,)
        score_text = font.render(f"Score : {self.score}", 1,(0,0,0))
        screen.blit(score_text,(20,20))

        # Appliquer l'Image du joueur :
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur :
        self.player.update_health_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Actualiser la barre d'événement du jeu
        self.comet_event.update_bar(screen)

        # Appliquer l'ensemble des images de mon groupe  de monstres :
        self.all_monsters.draw(screen)

        # Appliquer l'ensemble des images du gp de cometes
        self.comet_event.all_comets.draw(screen)

        # Recuperer les projectiles du joueur :
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Recuperer les monstres de notre jeu :
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Recuperer les cometes de notre jeu :
        for comet in self.comet_event.all_comets:
            comet.fall()


        # Appliquer l'ensemble des images e mon groupe ed projectiles
        self.player.all_projectiles.draw(screen)

        # Aller à droite et à gauche :
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False, pygame.sprite.collide_mask)

    def spawn_monster(self,monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
