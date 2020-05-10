# import pyautogui

# # color = (255, 255, 255)

# # # s = pyautogui.screenshot()
# # pyautogui.onScreen(1000, 200)

# # import numpy as np

# # zeros = np.zeros((100, 100), dtype=np.uint8)
# # zeros[:5,:5] = 255

# # indices = np.where(zeros == [255])
# # print(indices)
# # coordinates = zip(indices[0], indices[1])
# # print(coordinates)
# # import cv2
# # from PIL import Image
# # color = (235, 187, 7)
# # im = cv2.imread('sevenBtn.jpeg')
# # im = Image.open('sevenBtn.jpeg')
# # rgb_im = im.convert('RGB')
# # print(rgb_im)
# # for x in range(rgb_im.size()[0]):
# #     for y in range(rgb_im.size()[1]):
# #         r, g, b = rgb_im.getpixel((x, y))
# #         if (r,g,b) == colour:
# #             print(f"Found {colour} at {x},{y}!")

# import numpy as np
# import PIL
# import math

# # Load image and ensure RGB - just in case palettised
# im=PIL.Image.open("insta.png").convert("RGB")
# print(im)
# # Make numpy array from image
# npimage=np.array(im)
# # rgb(1,149,246)
# # Describe what a single red pixel looks like
# red=np.array([1,149,246])
# print(red)
# # Find [x,y] coordinates of all red pixels
# reds=np.where(np.all((npimage==red)))

# print(reds)

# print(blues)