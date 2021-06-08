#importation du module time
import time

#recuperer l heure
heure = time.strftime("%H heure %M minutes")

#afficher l heure
print("il est "+heure)

h = time.strftime("%H")

if(int(h)>13):
    print("Bonsoir")
else:
    print("Bonjour")

