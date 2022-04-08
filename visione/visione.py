from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely import affinity
import os
angolo_x=10
angolo_y= 10
posizione_macchina=(10,10)
vbs = Point (posizione_macchina[0]-angolo_x, posizione_macchina[1])
vbd = Point (posizione_macchina[0]+angolo_x, posizione_macchina[1])
vas = Point (posizione_macchina[0]-angolo_x, posizione_macchina[1]+angolo_y)
vad = Point (posizione_macchina[0]+angolo_x, posizione_macchina[1]+angolo_y)
rettangolo = Polygon([[p.x, p.y] for p in [vbs,vas,vad,vbd]]) 
ruotato= affinity.rotate(rettangolo, 180, 'center')
print(rettangolo.boundary)
print(ruotato.boundary)

def cv(landmarks):
    
    for x in range(len(landmarks)):
        #print(landmarks[x])
        if rettangolo.contains(landmarks[x]) :
            print(landmarks[x])


def carica_file(lista):
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


