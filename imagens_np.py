from PIL import  Image
import numpy as np

#Load image
def load_image( filename ):
    img = Image.open(filename)
    img.load()
    return img

#Convert image -> np
def image_to_numpy( img ):
    array_np = np.asarray( img, dtype="int32" )
    return array_np

img_insta = load_image('insta.png')
img_np = image_to_numpy(img_insta)


heigth = img_np.shape[0]
width = img_np.shape[1]
# print(heigth)
# print(width)

# print(img_np[heigth,width])
print(img_np[0][0][1])

# print(img_np.shape)
print('foi')

# for i in range(heigth):
    