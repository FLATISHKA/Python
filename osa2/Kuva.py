
import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")
x = 100
y = 200

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        kuva = pygame.image.load("image.png").convert()
        naytto.blit(kuva, (x, y))
        pygame.display.flip()

main()