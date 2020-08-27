import random
import string
import pygame

# Ikkunaohjelman rakenne
naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Mun peli")

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 0, 255), (0, 0), (640, 400))
        pygame.display.flip()

        naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 255, 0), (640, 0), (0, 400))
        pygame.display.flip()

main()