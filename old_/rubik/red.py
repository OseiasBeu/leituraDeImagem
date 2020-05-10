
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

M = Image.open("rubik.png")
M = np.asarray(M, dtype=np.float32)/255

# zera camada vermelha
M[:,:,0] = 0
# zera camada azul
M[:,:,1] = 0

# visualizando
plt.figure(figsize=(3, 3))
im = plt.imshow(M, aspect='auto')
plt.axis("off")
plt.show()