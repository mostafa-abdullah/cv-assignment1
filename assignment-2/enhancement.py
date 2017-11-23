import cv2
import numpy as np

from histogram import get_histogram, get_cumulative

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result/enhancement"

def contrast_stretch(img, low, high):
    """
    Perform constrast stretching on a given image
    :param img: The input image
    :param low: The lower limit of desired intensity range
    :param high: The upper limit of desired intensity range
    :return: The output image
    """
    cur_min, cur_max = img.min(), img.max()
    res = np.zeros(img.shape)
    scaling_factor = (high - low) / (cur_max - cur_min)
    for i in range(len(img)):
        for j in range(len(img[i])):
            res[i][j] = round((1 * img[i][j] - cur_min) * scaling_factor + low)

    return res


def histogram_equil(img, high):
    f = get_cumulative(get_histogram(img))
    f_min = f.min()
    pixels = len(img) * len(img[0])

    res = np.zeros(img.shape)
    for i in range(len(img)):
        for j in range(len(img[i])):
            equilized = (f[img[i][j]] - f_min) * high // (pixels - f_min)
            res[i][j] = equilized

    return res

if __name__ == '__main__':
    img = cv2.imread("{}/frostfog.png".format(IMAGES_FOLDER), 0)
    con_str_img = contrast_stretch(img, 0, 255)
    cv2.imwrite("{}/frostfog_con_str.png".format(OUTPUT_FOLDER), con_str_img)

    hist_img = histogram_equil(img, 255)
    cv2.imwrite("{}/frostfog_hist.png".format(OUTPUT_FOLDER), hist_img)
