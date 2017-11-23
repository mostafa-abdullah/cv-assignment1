import cv2

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result"

jb_img = cv2.imread("{}/james.png".format(IMAGES_FOLDER), 0)
london_img1 = cv2.imread("{}/london1.png".format(IMAGES_FOLDER), 0)
london_img2 = cv2.imread("{}/london2.png".format(IMAGES_FOLDER), 0)

current_img = 2

if current_img == 1:
    for i in range(len(jb_img)):
        for j in range(len(jb_img[i])):
            if jb_img[i][j] < 230:
                # Translate jb body to the left by 70 pixels
                london_img1[i][j - 70] = jb_img[i][j]

    cv2.imwrite("{}/london1.png".format(OUTPUT_FOLDER), london_img1)

if current_img == 2:
    for i in range(len(jb_img)):
        for j in range(len(jb_img[i])):
            if jb_img[i][j] < 230:
                # Flip (reflect) jb body horizontally
                london_img2[i][len(london_img2[i]) - j] = jb_img[i][j]

    cv2.imwrite("{}/london2.png".format(OUTPUT_FOLDER), london_img2)