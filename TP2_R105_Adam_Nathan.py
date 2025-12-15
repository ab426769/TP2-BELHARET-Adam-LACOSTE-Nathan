fic=open('Donnees.csv','r', encoding="utf-8")

ligne = []
for i in fic:
    i = i.strip("\n")
    i = i.split(';')
    ligne.append(i)
fic.close()


i = 0 #initie une nouvelle liste
j = 0
nouvelle_liste = []
while len(nouvelle_liste) < len(ligne):
	nouvelle_liste.append(ligne[i])
	i+=1

#---------------------------------------------------------------

#Pression en fonction de l'Altitude

pression = [] #créer une liste pour la pression
for i in range(len(nouvelle_liste)):
	pression.append(nouvelle_liste[i][8])
del pression[0]
L_P = [] #nouvelle liste pour avec les valeurs en float
for i in pression :
	i = float(i)
	L_P.append(i)

altitude = []
for i in range(len(nouvelle_liste)):
	altitude.append(nouvelle_liste[i][3])
del altitude[0]
L_A = []
for i in altitude :
	i = float(i)
	L_A.append(i)


from pylab import plot
from pylab import show
from matplotlib import pyplot as plt
plt.plot(L_A,L_P,color='b')
plt.title("Altitude en fonction de la pression")
plt.ylabel('Pression')
plt.xlabel('Altitude')
show()

#---------------------------------------------------------------

#Altitude en fonction du temps

def t_sec(temps): #fonction pour convertir le temps en secondes afin de pourvoir avoir le temps en float
    h, m, s = temps.split(':')
    return float(h) * 3600 + float(m) * 60 + float(s)

temps = []
for i in range(len(nouvelle_liste)):
	temps.append(nouvelle_liste[i][0])
del temps[0]
L_T = [] 
for i in temps :
	i = t_sec(i)
	L_T.append(i)

altitude = []
for i in range(len(nouvelle_liste)):
	altitude.append(nouvelle_liste[i][3])
del altitude[0]
L_A = []
for i in altitude :
	i = float(i)
	L_A.append(i)



from pylab import plot
from pylab import show
from matplotlib import pyplot as plt
plt.plot(L_T,L_A,color='b')
plt.title("Altitude en fonction du temps")
plt.ylabel('Altitude')
plt.xlabel('Temps')
show()

#-------------------------------------------------------------

#Latitude et Longitude en fonction du temps

temps = []
for i in range(len(nouvelle_liste)):
	temps.append(nouvelle_liste[i][0])
del temps[0]
L_T = [] 
for i in temps :
	i = t_sec(i)
	L_T.append(i)

Latitude = []
for i in range(len(nouvelle_liste)):
	Latitude.append(nouvelle_liste[i][1])
del Latitude[0]
L_LA = []
for i in Latitude :
	i = float(i)
	L_LA.append(i)

Longitude = []
for i in range(len(nouvelle_liste)):
	Longitude.append(nouvelle_liste[i][2])
del Longitude[0]
L_LO = []
for i in Longitude :
	i = float(i)
	L_LO.append(i)


from pylab import plot
from pylab import show
from matplotlib import pyplot as plt
plt.plot(L_T,L_LA,color='b')
plt.plot(L_T,L_LO,color='r')
plt.title("Latitude et Longitude en fonction du temps")
plt.ylabel('Latitude et Longitude')
plt.xlabel('Temps')
show()

#-------------------------------------------------------------

#importation des modules et déclaration des modules
import csv
import matplotlib.pyplot as plt
import time

raw_data = []

#--------------------------------------------------------------------------------

#fonctions d'extraction de traitement des données
def extraction(ayo) :
	raw_data = []
	liste = []

	fichier = open('Donnees.csv','r')
	for texte in fichier  :
		texte = texte.strip("\n")
		texte = texte.split(';')
		raw_data.append(texte)
	fichier.close()

	for y in range(len(raw_data)) :
		for x in range(len(raw_data[y])):
			if x == ayo :
				liste.append(raw_data[y][x])
			else :
				print
	return(liste)

def processing(oly) :
	liste2 = []
	del oly[0]
	for z in oly :
		z = float(z)
		liste2.append(z)
	return(liste2)

#--------------------------------------------------------------------------------


#choix de création du graphique
print("Température en fonction de l'atitude : [a]")
print("Humidité en fonction de la pression : [b]")
print("Veuillez choisir un graphique a générer ")

choix = input("\nVotre choix : ")
if choix == 'a' :
	print("Vous avez choisi : Température en fonction de l'altitude")
	print("Veuillez patienter le temps que nous créons votre graphique...")
	data_alt1 = extraction(3)
	data_in_temp1 = extraction(5)
	data_out_temp1 = extraction(6)

	data_alt2 = processing(data_alt1)
	data_in_temp2 = processing(data_in_temp1)
	data_out_temp2 = processing(data_out_temp1)

elif choix == 'b' :
	print("Vous avez choisi : Humidité en fonction de la pression")
	print("Veuillez patienter le temps que nous créons votre graphique...")
	data_press1 = extraction(8)
	data_humid1 = extraction(7)

	data_press2 = processing(data_press1)
	data_humid2 = processing(data_humid1)

else :
	print("Graphique non disponible")

#--------------------------------------------------------------------------------


#création du graphique demandé
if choix == 'a' :
	time.sleep(3)
	plt.plot(data_alt2,data_in_temp2, label = "temp. interieur",color = 'blue')
	plt.plot(data_alt2,data_out_temp2, label = "temp. exterieur",color = 'orange')
	plt.xlabel("altitude")
	plt.ylabel("témperature")
	plt.title("températures en fonction de l'altitude")
	plt.legend()
	plt.show()

elif choix == 'b' :
	time.sleep(3)
	plt.plot(data_press2,data_humid2, color = 'red')
	plt.xlabel("pression")
	plt.ylabel("humidité")
	plt.title("humidité en fonction de la pression")
	plt.show()



