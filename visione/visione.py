
def cv(pose,landmarks):
    angolo_x=6
    angolo_y= 11
    for x in range(len(landmarks)):
        if landmarks[x][0] in range(pose[0]-angolo_x,pose[0]+angolo_x) and landmarks[x][1] in  range(pose[1]+1,pose[1]+angolo_y):
            print(landmarks[x])
def carica_file(lista):
    file_coni = open("C:\\Users\\Tano\\Desktop\\visione\\posizione.txt")
    for line in file_coni:
        line2 = file_coni.readline()
        lista.append((int(line), int(line2)))
        if 'str' in line:
            break
    file_coni.close()
    


##MAIN##
coni = []
carica_file(coni)
posizione_macchina=(10,10)
print(coni[0])
cv(posizione_macchina,coni)


