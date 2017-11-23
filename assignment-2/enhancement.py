import cv2
import numpy as np

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result/enhancement"

def contrast_stretch(img, low, high):
    cur_min, cur_max = img.min(), img.max()
    res = np.zeros(img.shape)
    scaling_factor = (high - low) / (cur_max - cur_min)
    for i in range(len(img)):
        for j in range(len(img[i])):
            res[i][j] = round((1 * img[i][j] - cur_min) * scaling_factor + low)

    return res


if __name__ == '__main__':
    img = cv2.imread("{}/frostfog.png".format(IMAGES_FOLDER), 0)
    con_str_img = contrast_stretch(img, 0, 255)
    cv2.imwrite("{}/frostfog_con_str.png".format(OUTPUT_FOLDER), con_str_img)
