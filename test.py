import random
from Voiture import*
def calculerTonAge():
    ageInf1 = random.random()
    age = int(ageInf1*100)
    print("Tu as"+str(age)+"ans")
    return age

compteur = 0


"""while(True):
    age = calculerTonAge()
    compteur+=1
    if age == 99:
        print("T'es vieux gros")
        print(str(compteur)+"essai(s)")
        break

    age = int(ageInf1*100)
    if(age == 100):
        print("Tu as " + age + " ans")

while(True) :
    calculerTonAge()"""

ma1erVoiture = Voiture()
ma1erVoiture._set_roues(5)
ma1erVoiture._get_roues()
