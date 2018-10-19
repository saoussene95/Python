phrase= input ("Entrer une phrase : ")
saisie= input ("Entrer une lettre: ")
nombre=0
for lettre in phrase:
    if lettre == saisie:
        nombre +=1
print (" la phrase saisie comporte ", nombre ,saisie)

