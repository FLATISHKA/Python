import random
import string

# Satunnaisuus
print(random.randint(1, 10))

# Nopan heittäminen
## print("Silmäluku: " + str(random.randint(1, 6)))
print("Silmäluku: ", random.randint(1, 6))

#Kolikon heittäminen
a = ["kruuna", "klaava"]
print("Tulos: " + random.choice(a))

# Salasanan arpoja
##merkkimaara = 0
##salasana = ""
##while(merkkimaara<8):
##    salasana += random.choice(string.ascii_lowercase)
##    merkkimaara +=1
##print("Salasana: ", salasana)

salasana=""
for x in range(8):
    salasana += random.choice(string.ascii_lowercase)
print("Salasana: ", salasana)

# Sekoittaja
luvut = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(luvut)
print(luvut)

# Vihollisen sijainnit
sijaintiLista = []
for i in range(1, 1000):
    n = str(random.randint(1,100)) + "," + str(random.randint(1,100))
    sijaintiLista.append(n)
print(sijaintiLista)