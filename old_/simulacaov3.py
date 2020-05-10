from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

M = Image.open('insta.png')
M = np.asarray(M,dtype=np.float32)/255

# zera camada vermelha
M[940:290,:,0] = 0
# zera camada azul
M[940:290,:,1] = 0
M[940:290,:,2] = 0




plt.figure(figsize=(3,3))
im = plt.imshow(M,aspect='auto')
plt.axis("off")
plt.show()
