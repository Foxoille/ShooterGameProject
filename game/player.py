import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite) :

    def __init__(self,game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 480

    def damage(self,amount):

        if self.health - amount > amount :
            # infliger des degats
            self.health -= amount

        else :
            # Si le joueur n'as plus de points de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()
        self.image = pygame.transform.scale(self.image, (200, 200))

    def update_health_bar(self, surface):

        # Dessiner la barre de vie
        pygame.draw.rect(surface, (60,63,60), [self.rect.x +48, self.rect.y -20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46),[self.rect.x +48, self.rect.y -20, self.health, 5])


    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectille
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_menager.play('tir')



    def move_right(self):
        # Si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity

