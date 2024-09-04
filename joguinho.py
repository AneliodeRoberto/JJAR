import pygame
pygame.init()
#tela
pygame.display.set_mode((430,680))
pygame.display.set_caption("eu sou anelio")
#loop
while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            pygame.quit()
            exit()
