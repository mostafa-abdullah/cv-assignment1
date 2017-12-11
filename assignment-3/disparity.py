import cv2
import numpy as np

IMAGES_FOLDER = "images/disparity"
RESULT_FOLDER = "result/disparity"


def calculate_SAD(img1, img2, pos1, pos2, window):
    res = 0
    for addi in range(-window // 2, window // 2):
        for addj in range(-window // 2, window // 2):
            if pos1[0] + addi < 0 or pos1[1] + addj < 0:
                continue
            if pos2[0] + addi < 0 or pos2[1] + addj < 0:
                continue
            if pos1[0] + addi >= len(img1) or pos1[1] + addj >= len(img1[0]):
                continue
            if pos2[0] + addi >= len(img1) or pos2[1] + addj >= len(img1[0]):
                continue
            res += abs(0 + img1[pos1[0] + addi][pos1[1] + addj] - img2[pos2[0] + addi][pos2[1] + addj])
    return res


def estimate_disparity(img1, img2, window, disparity_range):
    if img1.shape != img2.shape:
        raise ValueError("The two images should have the same dimensions")

    res = np.zeros(img1.shape)
    for i in range(len(img1)):
        for j in range(len(img1[i])):
            min_val = (window + 1) * (window + 1) * 255
            for i2 in range(i + disparity_range[0], i + disparity_range[1]):
                for j2 in range(j + disparity_range[2], j + disparity_range[3]):
                    SAD = calculate_SAD(img1, img2, (i, j), (i2, j2), window)

                    min_val = min(min_val, SAD)

            res[i][j] = min_val

    return res


def write_disparity(img_name):
    print("START {}".format(img_name))
    img1 = cv2.imread("{}/{}/img_1.png".format(IMAGES_FOLDER, img_name), 0)
    img2 = cv2.imread("{}/{}/img_2.png".format(IMAGES_FOLDER, img_name), 0)

    res = estimate_disparity(img1, img2, 3, (0, 1, 0, 1))

    cv2.imwrite("{}/{}.png".format(RESULT_FOLDER, img_name), res)
    print("DONE {}".format(img_name))

write_disparity("cones")
write_disparity("teddy")

