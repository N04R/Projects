import random   

prenom="noah"
age=21
print(f'je m"appele {prenom} et j"ai {age} ans')

anne_naissance=2004
anne_courante=2025

print(f'age = {anne_courante-anne_naissance}')

print(f"année depuis 18 ans = {anne_courante-anne_naissance-18}")

if age % 2 == 0:
    print(f'votre age est pair')
else : 
    print(f'va te faire enculer')


for i in range(1,11):
    if i % 2 == 0:
        print(f'{i} est pair')
    else:
        print(f'{i} est impair') 
    i+=1

n = 5 
somme=0
for i in range (1,n+1):
    somme+=i
    print(somme)

print(sum(range(1,n+1)))

n=7
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
    i+=1

liste_nombre= [10,20,30,40,50]
print(liste_nombre[0],liste_nombre[2],liste_nombre[-1])

liste_nom = ["bob","anna","jacques","pascal"]
liste_nom.reverse()
print(liste_nom)
print(list(reversed(liste_nom)))
liste_nom.sort()
print(liste_nom)
print(list(sorted(liste_nom)))
carré_pairs=[x**2 for x in range (1,11) if x % 2 == 0]
print(carré_pairs)

aléatoire_100=[random.randint(0,100) for _ in range(100)]
print(aléatoire_100)
print(f'{sum(aléatoire_100)/len(aléatoire_100)}')