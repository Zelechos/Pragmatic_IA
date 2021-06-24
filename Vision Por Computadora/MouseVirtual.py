import cv2
import numpy as np
import SeguimientoManos as sm
import autopy


anchocam, altocam = 640 , 480
cuadro = 100
anchopanta, altopanta = autopy.screen.size()
sua = 5
pubix ,pubiy = 0,0
cubix, cubiy = 0,0

cap = cv2.VideoCapture(0)
cap.set(3,anchocam)
cap.set(4,altocam)

detector = sm.detectormanos(maxManos = 1)

while True:
    ret , frame = cap.read()
    frame = detector.encontrarmanos(frame)
    lista , bbox =detector.encontrarposicion(frame)
    
    if len(lista) !=0:
        x1 ,y1 =lista[8][1:]
        x2 ,y2 =lista[12][1:]
        
        dedos =detector.dedosarriba()
        
        cv2.rectangle(frame, (cuadro,cuadro), (anchocam - cuadro , altocam - cuadro),(0,0,0),2)
        
        if dedos[1]==1 and dedos[2]==0:
            
            x3 = np.interp(x1, (cuadro, anchocam - cuadro), (0, anchopanta))
            y3 = np.interp(y1, (cuadro, altocam - cuadro), (0, altopanta))
            
            cubix = pubix + (x3- pubix)/sua
            cubiy = pubiy + (y3- pubiy)/sua
            
            autopy.mouse.move(anchopanta - cubix ,cubiy)
            cv2.circle(frame,(x1,y1), 10, (0,0,0), cv2.FILLED )
            pubix ,pubiy = cubix , cubiy
    
        if dedos[1]==1 and dedos[2] == 1:
            
            longitud , frame , linea = detector.distancia(8,12,frame)
            print(longitud)
            if longitud < 30:
                cv2.circle(frame, (linea[4],linea[5]), 10, (0,255,0), cv2.FILLED)
                
                autopy.mouse.click()




    cv2.imshow("mouse",frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
