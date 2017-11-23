import cv2
import numpy as np
IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result"

img1 = cv2.imread("{}/tree.png".format(IMAGES_FOLDER), 0)
img2 = cv2.imread("{}/treeM.png".format(IMAGES_FOLDER), 0)

diff = np.absolute((img2 - img1) * 50)

cv2.imwrite("{}/mystery.png".format(OUTPUT_FOLDER), diff)
