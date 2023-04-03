from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely import affinity
import os
ANGOLO_X=10
ANGOLO_Y= 10
posizione_macchina= Point(10,10)
orientamento_macchina = 0
vas = Point (posizione_macchina.x-ANGOLO_X, posizione_macchina.y+ANGOLO_Y)
vad = Point (posizione_macchina.x+ANGOLO_X, posizione_macchina.y+ANGOLO_Y)
triangolo = Polygon([[p.x, p.y] for p in [posizione_macchina, vas, vad]]) #i punti del poligono vano messi in ordine in cui va disegnato
ruotato= affinity.rotate(triangolo, orientamento_macchina, posizione_macchina)  #l'angolo di rotazione ruota in senso antiorario
print(triangolo.boundary)
print(ruotato.boundary)

def cv(landmarks): #funzione che controlla se un cono si trova all'interno del triangolo di visione 
    
    for x in range(len(landmarks)):
        if triangolo.contains(landmarks[x]) :
            print("Vedo i coni in posizione:\n", landmarks[x], "\n")


def carica_file(lista): #funzione per caricare dal file la lista dei coni
    location_coni = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_coni = open(os.path.join(location_coni, 'posizione.txt'))
    for line in file_coni:
        line2 = file_coni.readline()
        cono = Point(int(line), int(line2))
        lista.append(cono)
        if 'str' in line:
            break
    file_coni.close()
    


##MAIN##
coni = []
carica_file(coni)
cv(coni)


