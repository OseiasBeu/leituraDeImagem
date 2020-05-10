# importando a biblioteca PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# lendo o arquivo rubik.jpg
M = Image.open("rubik.png")

# transformando para Numpy array
M = np.asarray(M, dtype=np.float32)/255

# visualizando
plt.figure(figsize=(3, 3))
im = plt.imshow(M, aspect='auto')
plt.axis("off")
plt.show()