import cv2

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result"

current_exercise = 3

# Ex. 1 -- Dimming
if current_exercise == 1:
    guc_img = cv2.imread("{}/GUC.png".format(IMAGES_FOLDER), 0)
    for i in range(len(guc_img)):
        for j in range(len(guc_img[i])):
            guc_img[i][j] = max(0, guc_img[i][j] - 70)
    cv2.imwrite("{}/GUC.png".format(OUTPUT_FOLDER), guc_img)

# Ex. 2 -- Shadow Removal
if current_exercise == 2:
    calc_img = cv2.imread("{}/calculator.png".format(IMAGES_FOLDER), 0)
    # Check whether last pixel was white and haven't entered the calculator borders yet
    for i in range(len(calc_img)):
        for j in range(1, len(calc_img[i])):
            if calc_img[i][j - 1] >= 240:
                # last pixel was white
                if calc_img[i][j] >= 175:
                    # this pixel is a shadow
                    calc_img[i][j] = 255
                else:
                    # Entered calculator borders; move on to the next row
                    break
    cv2.imwrite("{}/calculator.png".format(OUTPUT_FOLDER), calc_img)

# Ex. 3 -- Partial brightening
if current_exercise == 3:
    cameraman_img = cv2.imread("{}/cameraman.png".format(IMAGES_FOLDER), 0)
    for i in range(len(cameraman_img)):
        for j in range(len(cameraman_img[i])):
            if cameraman_img[i][j] < 70:
                cameraman_img[i][j] += 50

    cv2.imwrite("{}/cameraman2.png".format(OUTPUT_FOLDER), cameraman_img)





