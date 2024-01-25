import pygame
from pygame.locals import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SPEED = 10
GRAVITY = 1


class Bird(pygame.sprite.Sprite):  # criando classe herdando dessa biblioteca feita paar imagens

    def __init__(self):  # função obrigatoria quando criar a classe
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load(  # crinado lista de imagens para movimento
            'FlappyBird/imgs/bird1.png').convert_alpha(),
            pygame.image.load(
            'FlappyBird/imgs/bird2.png').convert_alpha(),
            pygame.image.load(
            'FlappyBird/imgs/bird3.png').convert_alpha()]

        self.speed = SPEED

        self.current_image = 0  # contador aux de imagem para att de movimento

        self.image = pygame.image.load(
            'FlappyBird/imgs/bird1.png').convert_alpha()  # criando imagem do passaro

        # orientando onde o passaro deve estar rect é onde o passaro deve estar
        self.rect = self.image.get_rect()
        # orientando x,y de onde passaro estara, com rect iremos controlar onde esta o passaro e a altura
        self.rect[0] = SCREEN_WIDTH / 2
        # orientando x,y de onde passaro estara
        self.rect[1] = SCREEN_HEIGHT / 2

        print(self.rect)  # mostrando o passaro criado

    def update(self):  # FRAMES DO GAME
        # com isso cria o ciclio, quando chegar em imagem 3, ele volta ao zero, MOVIMENTO DO PASSARO
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        self.speed += GRAVITY

        # Update height

        self.rect[1] += self.speed

    def bump(self):  # crinado pulo com logica
        self.speed = -SPEED

# criando tela


# iniciando o pygame, orbigatorio em todo jogo
pygame.init()
# criando tela do jogo com a função display.set_mode, ela recebe uma tupla

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

# criando background com load e o nome do arquivo + caminho
BACKGROUND = pygame.image.load('FlappyBird/imgs/bg.png')
# tendo certeza que minha escala sera do tamanho da tela, recbe uma tupla com o tamaho da tela
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_WIDTH))

# crinado grupo para ajudar no gerenciamento de objetos
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)  # adicioando ao grupo criado


clock = pygame.time.Clock()  # com clock podemos ajudar a controlar  fps
# criando laço principal onde ficara atalizando todos os eventos
while True:
    clock.tick(30)  # com o comando tick podemos limitar a 30 fps

    for event in pygame.event.get():  # criando teste de eventos
        if event.type == QUIT:  # se o evento for de quit, pygame.quit()
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    # atualizando o backgtound na tela a cada evento, passamos o fundo + tupla com as coordenadas de onde ira começar a imagem
    screen.blit(BACKGROUND, (0, 0))

    bird_group.update()  # atualizando grupo
    # desesnhando grupo com varios elementos, passando superficie
    bird_group.draw(screen)  # desenahndo passaro na tela
    pygame.display.update()  # depois de cada evento, ele atualiza a tela
