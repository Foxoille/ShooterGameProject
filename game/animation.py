import pygame

# Definir une class qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # Definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name, size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image,size)
        self.current_image = 0 # Commencer l'anim à l'image 0
        self.images = animation.get(sprite_name)
        self.animation = False


    # Definir une methode pour demarer l'animation
    def start_animation(self):
        self.animation= True


    # Definir une methode pour animer le Sprite
    def animate(self,loop =False):

        # Verifier si l'naimation est active
        if self.animation :


            # Passer à l'image suivante
            self.current_image += 1

            # Verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # Remettre l'animaiton au départ
                self.current_image = 0

                # Verifier si l'animation n'est pas en mode boucle
                if loop is False :
                    self.animation = False

            # Modifier l'image de l'animation précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# Definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # Charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # Recuperer le chemin du dossier pour ce Sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # Boucler sur chaque ficher chaque image dans ce dossier
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # Revenvoyer le contenu
    return images


# Definir un dictionnaire qui vas contenir les images chargés de chaque sprite
# mummy -> [mummy1.png,...]
animation = {
    'mummy' : load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien' : load_animation_images('alien')
}
