import random
print('this is a test')
babas = "gay"




def calculerTonAge():
    ageInf1 = random.random()

    age = int(ageInf1*100)
    print("Tu as"+str(age)+"ans")
    return age

compteur = 0

while(True):
    age = calculerTonAge()
    compteur+=1
    if age == 99:
        print("T'es vieux gros")
        print(str(compteur)+"essai(s)")
        break
