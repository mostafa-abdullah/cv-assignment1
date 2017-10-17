import cv2
import numpy as np

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result"

lake_img = cv2.imread("{}/lake.png".format(IMAGES_FOLDER), 0)
res_img = np.empty_like(lake_img)

for i in range(len(lake_img)):
    for j in range(len(lake_img[i])):
        # construct a 3x3 mask
        startRow = max(0, i - 1)
        endRow = min(len(lake_img), i + 1)
        startCol = max(0, j - 1)
        endCol = min(len(lake_img[i]), j + 1)

        # Get the variance at the current pixel with this mask
        variance = np.var(lake_img[startRow: endRow, startCol: endCol])

        # Smooth lake will likely have low variance < 30
        # Keep ducks with color > 200
        if variance < 30 and lake_img[i][j] < 200:
            res_img[i][j] = 0
        else:
            res_img[i][j] = lake_img[i][j]

cv2.imwrite("{}/lake.png".format(OUTPUT_FOLDER), res_img)

