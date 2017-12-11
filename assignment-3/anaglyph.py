import cv2
import numpy as np

IMAGES_FOLDER = "images/anaglyph"
RESULT_FOLDER = "result/anaglyph"


def get_anaglyph(img, offset=5):
    res = np.zeros(img.shape)
    for i in range(len(img)):
        for j in range(len(img[i])):
            res[i][j][0] = img[i][j][0]
            res[i][j][1] = img[i][j][1]
            if j - offset >= 0:
                res[i][j][2] = img[i][j - offset][2]
            else:
                res[i][j][2] = img[i][0][2]
    return res


def write_anaglyph(img_path):
    print("START {}".format(img_path))
    img = cv2.imread("{}/{}".format(IMAGES_FOLDER, img_path))
    anag = get_anaglyph(img, 10)

    cv2.imwrite("{}/{}".format(RESULT_FOLDER, img_path), anag)
    print("DONE {}".format(img_path))

if __name__ == '__main__':
    write_anaglyph("1984.jpg")
    write_anaglyph("creed.jpg")
    write_anaglyph("tree.jpg")
