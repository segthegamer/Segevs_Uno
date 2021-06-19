import pygame
pygame.init()

# Game window
Screen_Width = 1200
Screen_Height = 600
screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# Constants
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 128)
Red = (256, 0, 0)
LeftMouse = 1
MiddleMouse = 2
RightMouse = 3

# Background image
def RedrawWindow():
    #    backround = pygame.image.load('background.png')
    #    screen.blit(backround, (0, 0))
    screen.fill(White)
    pygame.display.update()


def DrawCard(type, color):
    make_image = color + "_" + type + ".png"
    card_image = pygame.image.load(make_image)
    card_image.convert()

    rect = card_image.get_rect()
    rect.center = Screen_Width // 2, Screen_Height // 2

    screen.blit(card_image, rect)
    pygame.display.update()

def Game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            RedrawWindow()
            type = input("Enter type")
            color = input("Enter color")
            DrawCard(type, color)

Game()