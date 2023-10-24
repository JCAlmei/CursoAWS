print("Seja bem vindo ao Hotel!\n")
print("A sequencia abaixo imprime os andares do predio que irá visitar: \n")
print("**Sequência utilizando laço 'For'.**\n")

andar = 20

for andar in range(20):
    andar = andar + 1
    if (andar == 13):
        continue
    print(str(andar) + "° Andar")

print("\nEm seguida a sequencia inververtada de andares: \n")

for andar in range((andar), 0, -1):
    if (andar == 13):
        continue
    print(str(andar) + "° Andar")

print("\n**Sequência utilizando laço 'While'.**\n")
print("A sequencia abaixo imprime os andares do predio que irá visitar: \n")

andar=0
while andar < 20:
    andar += 1

    if andar == 13:
        continue

    print(str(andar) + "° Andar")