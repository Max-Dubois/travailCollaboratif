import random
import numpy as np

#v1
print ("Version 1")
Nbmax=int(input("Entrez nbMax :  "))
compteur=0
liste=[]
passage=0
while(compteur<Nbmax):
    x = random.randint(0,1000)
    if x%2==0 :
          liste=liste+[x]
          compteur=compteur+1
    passage=passage+1

print(f"il a fallu {passage} passages dans la boucle for pour obtenir {Nbmax} nombres pairs")
print(f"liste={liste}")

#v2
print("Version 2")
Nbmax=int(input("Entrez nbMax :  "))
compteur=0
liste=[]
passage=0
while(compteur<Nbmax):
    x = random.randint(0,1000)
    if x%2==0 :
          liste=liste+[x]
          compteur=compteur+1
    passage=passage+1

print(f"il a fallu {passage} passages dans la boucle for pour obtenir {Nbmax} nombres pairs")
print(f"liste={liste}")

#v3
print("Version 3")

Nbmax=int(input("Entrez nbMax :  "))
compteur=0
liste=[]
passage=0
while(compteur<Nbmax):
    x = random.randint(0,1000)
    if x%2==0 :
          liste=liste+[x]
          compteur=compteur+1
    passage=passage+1

print(f"il a fallu {passage} passages dans la boucle for pour obtenir {Nbmax} nombres pairs")
print(f"liste={np.sort(liste)}")