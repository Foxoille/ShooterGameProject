""" Les Imports : """
import pygame
import math
from game import Game
pygame.init()


""" Le Programme : """

# Definir une clock
clock = pygame.time.Clock()
FPS = 60

# Generation de la fênetre du jeu :
pygame.display.set_caption("Commet Fall Game")
screen = pygame.display.set_mode((1080,700))


# importation de l'arrière plan du jeu:
background = pygame.image.load('assets/bg.jpg')

# Importer et charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Import/ charger notre bouton popur lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

# Charger le Jeu :
game = Game()


# Boucle tant que : Garder le jeu allumé :

running = True
while running :

    # Application de l'arrière plan :
    screen.blit(background,(0,-200))

    # Verifier si notre jeu a commencé ou non
    if game.is_playing:
        # Declencher les instruction de la partie
        game.update(screen)

    # Verifier si notre jeu n'as pas commencé
    else :
        # Ajouter l'écran de bienvenue
        screen.blit(play_button,(play_button_rect.x,play_button_rect.y))
        screen.blit(banner,banner_rect)

    # Mettre a jour l'ecran:
    pygame.display.flip()

    # Gestion d'Evenements
    for event in pygame.event.get():

        # que l'évenement est fermeture de fênetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du Jeu")

        # Detecter touches :

        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True

            # Detecter si la touche espace est enclenchée pour lancer notre projectille

            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else :
                    # Mettre le jeu en mode "lancé"
                    game.start()
                    # Jouer le son
                    game.sound_menager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN :
            # Verifier si on clique sur le bouton
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode "lancé"
                game.start()
                # Jouer le son
                game.sound_menager.play('click')

    # Fixer le nombre de FPS sur ma  clock
    clock.tick(FPS)