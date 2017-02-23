import random

def calculerTonAge():
    ageInf1 = random.random()
    age = int(ageInf1*100)
    if(age == 100):
        print("Tu as " + age + " ans")

while(True) :
    calculerTonAge()
