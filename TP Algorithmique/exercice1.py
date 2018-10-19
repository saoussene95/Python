phrase= input ("Entrer une phrase : ")
nombre=0
for lettre in phrase:
    if lettre != " ":
        nombre +=1

print ("La phrase comporte donc ",nombre,"lettres");
