numero = 0
for i in range(21):
 numero = numero + 1
 if (numero == 13):
  continue
 if (numero == 21):
  break
 print(numero)

numero = 21
for i in range(21,0,-1):
 numero = numero - 1
 if (numero == 13):
  continue
 if (numero == 0):
  break
 print(numero)


i = 0
while (i <= 21):
    i = i + 1
    if (i == 13):
        continue
    if (i == 21):
        break
    print(i)

i = 21
while (i >= 0):
    i = i - 1
    if (i == 13):
        continue
    if (i == 0):
        break
    print(i) 