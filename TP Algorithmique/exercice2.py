phrase= input ("Entrer une phrase : ").lower()
nombre=0
listeVoyelle =("a", "e" ,"i", "o", "u", "y")
for lettre in phrase:
    if lettre in listeVoyelle:
        nombre +=1
print (" la phrase saisie comporte ", nombre , "voyelles")
