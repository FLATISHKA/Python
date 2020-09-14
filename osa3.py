import pygame
import random
naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")

def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            kuva = pygame.image.load(vihollinen[0]).convert()
            naytto.blit(kuva, (vihollinen[1], vihollinen[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma, viholliset):
    for vihollinen in viholliset:
        if hahmot[0][1] == vihollinen[1] and hahmot[0][2] == vihollinen[2]:
            del hahmot[0]

        if viholliset[0][1] > 640:
            viholliset[0][1] = 0
            viholliset[0][2] = random.randrange(0, 360, 10)
        else:
            viholliset[0][1] += 1

        if viholliset[1][1] > 640:
            viholliset[1][1] = 0
            viholliset[1][2] = random.randrange(0, 360, 10)
        else:
            viholliset[1][1] += 1

        if viholliset[2][1] > 640:
            viholliset[2][1] = 0
            viholliset[2][2] = random.randrange(0, 360, 10)
        else:
            viholliset[2][1] += 0.5

    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
        elif tapahtuma.key == pygame.K_RIGHT and hahmot[0][1] < 610:
            hahmot[0][1] += 10
        elif tapahtuma.key == pygame.K_LEFT and hahmot[0][1] > 10:
            hahmot[0][1] -= 10
        elif tapahtuma.key == pygame.K_UP and hahmot[0][2] > 10:
            hahmot[0][2] -= 10
        elif tapahtuma.key == pygame.K_DOWN and hahmot[0][2] < 360:
            hahmot[0][2] += 10
        viholliset[0][3] = True
        viholliset[1][3] = True
        viholliset[2][3] = True



def main():
    hyvis = ["hyvis.png", 200, 100, False]
    pahis1 = ["pahis.png", 100, 50, False]
    pahis2 = ["pahis.png", 470, 200, False]
    pahis3 = ["pahis.png", 240, 300, False]
    hahmot = [hyvis]
    viholliset = [pahis1, pahis2, pahis3]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)


main()



    