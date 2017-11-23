import cv2
import time
import numpy as np
import math

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result/remove_noise"

def median(img, i, j, size):
    """
    Apply median kernel of a given size on cell (i,j) in an image
    """
    row_low, row_high = max(0, i - size), min(len(img) - 1, i + size)
    col_high = min(len(img[i]) - 1, j + size)

    vals = []  # Values in the kernel
    while(row_low <= row_high):
        col_low = max(0, j - size)
        while(col_low <= col_high):
            vals.append(img[row_low][col_low])
            col_low += 1
        row_low += 1
    vals.sort()

    # Middle value if odd length, else mean of middle values
    if len(vals) % 2:
        return vals[len(vals) // 2]
    return round((1 * vals[len(vals) // 2] + vals[len(vals) // 2 + 1]) / 2)

def remove_noise(image_name, method="median", limit_low=-1, limit_high=-1):
    img = cv2.imread("{}/{}.png".format(IMAGES_FOLDER, image_name), 0)
    img_res = np.zeros(img.shape)
    size = 2
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] >= limit_low and img[i][j] <= limit_high:
                img_res[i][j] = img[i][j]
            else:
                row_low, row_high = max(0, i - size), min(len(img), i + size + 1)
                col_high = min(len(img[i]), j + size + 1)
                col_low = max(0, j - size)

                img_res[i][j] = median(img, i, j, size)

    cv2.imwrite("{}/{}_{}.png".format(OUTPUT_FOLDER, image_name, method), img_res)

if __name__ == '__main__':
    start_time = time.time()
    remove_noise("fognoise")
    end_time = time.time()
    print("Ran median filter in {} seconds".format(end_time - start_time))

    start_time = time.time()
    remove_noise("fognoise", limit_low=70, limit_high=200, method="hist")
    end_time = time.time()
    print("Ran median filter with limits in {} seconds".format(end_time - start_time))
