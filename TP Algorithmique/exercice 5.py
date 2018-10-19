saisie = input (" ecrivez une phrase :")
inverse = ""
for i in saisie:
    inverse = i + inverse
if saisie == inverse:
    print ("c'est un palindrome")
else:
    print ("ce n'est pas un palindrome")
