from  PIL import Image
import sys
import numpy as np

img = Image.open('insta.png') #Faz a leitura da imagem (imagem da tela de entrar do instagram doi utilizada aqui)
width, height = img.size[:2] #Segrega a altura e a largura
px = np.array(img) #Converte a imagem em array

for y in range(height): #Loop responsável por varrer a imagem na vertical
    for x in range(width): #Loop responsável por varrer a imagem na horizontal
        if px[y,x,0] == 70 and px[y,x,1] == 110 and px[y,x,2] == 251: #verifica se os valores em RGB existem na posição do array
            print(y,x,px[y,x,0],px[y,x,1],px[y,x,2])
            print('Par ordenado:\nX:{}\nY:{}'.format(x,y))
            sys.exit()
       
            