from bepro import *
from bordes import *
import matplotlib.pyplot as plt
#Esto es un preprocesamiento de la tarea1
img=cv2.imread('Entrada.png',1) #imagen original
img2=gris(img)
img3=gauss(img2)
m, an, datos, grax, gray=prewitt(img3)
umb=100
ima2=borde(m,umb,img3)


#img2 es la imagen binarizada preprocesada en deteccion de bordes.
#gx, gy son matrices cuyos elementos corresponden al gradiente en sus
#respectivos ejes.
h, w = ima2.shape
freq = dict()
lines = dict()
discr=5 #valor de discretización
datos2=[]
for h1 in xrange(0,h,1):
    for w1 in xrange(0,w,1):
        #se accede a los pixeles detectados como borde
        if ima2[h1,w1]!=0:
            # se establece una reestriccion para garantizar angulos de 0
            # y 90 grados
            if grax[h1,w1] > 0 and gray[h1,w1] == 0:
                theta = 0
            elif grax[h1,w1] < 0 and gray[h1,w1] == 0:
                theta = 180
            if grax[h1,w1] == 0 and gray[h1,w1] > 0:
                theta = 90
            elif grax[h1,w1] == 0 and gray[h1,w1] < 0:
                theta = 270
            else:
                theta = (int(math.degrees(math.atan2(gray[h1,w1],grax[h1,w1])))/discr)*discr
            # se calcula el valor de ro, para posteriormente calcular la ecuación
            # de la recta.
            ro = (int((w1*math.cos(theta)) + (h1*math.sin(theta)))/discr)*discr
            lines[h1,w1] = (theta, ro)
            datos2.append(ro)
            
            if theta == 0.0 or theta == 180.0:
                img[h1,w1] = (0, 255, 0)
            elif theta == 90.0 or theta == 270.0:
                img[h1,w1] = (0, 0, 255)
            else:
                img[h1,w1] = (255, 0, 0) 
            


plt.hist(datos2,bins=10,color='green',alpha=0.1)
plt.xlabel('Magnitudes')
plt.ylabel('Freuencias')
plt.title('histograma')
plt.show()

cv2.imshow('Lineas',img)
cv2.imwrite('pruebao.jpg',ima2)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()


