import pygame

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
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
        elif tapahtuma.key == pygame.K_RIGHT and hahmot[0][1] < 580:
            hahmot[0][1] += 10
        elif tapahtuma.key == pygame.K_LEFT and hahmot[0][1] > -30:
            hahmot[0][1] -= 10
        elif tapahtuma.key == pygame.K_UP and hahmot[0][2] > -30:
            hahmot[0][2] -= 10
        elif tapahtuma.key == pygame.K_DOWN and hahmot[0][2] < 350:
            hahmot[0][2] += 10
        viholliset[0][3] = True

def main():
    hyvis = ["hyvis.png", 200, 100, False]
    pahis = ["pahis.png", 100, 100, False]
    hahmot = [hyvis]
    viholliset = [pahis]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)


main()



    