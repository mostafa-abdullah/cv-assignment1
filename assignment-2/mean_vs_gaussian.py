import cv2
from histogram import plot_data

IMAGES_FOLDER = "images"
RESULT_FOLDER = "result"
MEAN_FOLDER = RESULT_FOLDER + "/mean"
MEAN_HIST_FOLDER = MEAN_FOLDER + "/hist"
GAUSS_FOLDER = RESULT_FOLDER + "/gauss"
GAUSS_HIST_FOLDER = GAUSS_FOLDER + "/hist"

def mean_filter(img, size):
    """
    Apply the mean blurring kernel on a given image
    :param img: The input image
    :param size: The size of the kernel
    :return: The image after applting the filter on
    """
    return cv2.blur(img, (size, size))

def gauss_filter(img, size):
    """
    Apply the gauss blurring kernel on a given image
    :param img: The input image
    :param size: The size of the kernel
    :return: The image after applting the filter on
    """
    return cv2.GaussianBlur(img,(size, size),0)


def mean_vs_gauss(image_name):
    img = cv2.imread("{}/{}.png".format(IMAGES_FOLDER, image_name), 0)

    img_mean = mean_filter(img, 5)
    img_gauss = gauss_filter(img, 5)

    cv2.imwrite("{}/{}.png".format(MEAN_FOLDER, image_name), img_mean)
    cv2.imwrite("{}/{}.png".format(GAUSS_FOLDER, image_name), img_gauss)

    plot_data(img_mean, "{}/{}.png".format(MEAN_HIST_FOLDER, image_name))
    plot_data(img_gauss, "{}/{}.png".format(GAUSS_HIST_FOLDER, image_name))


if __name__ == '__main__':
    mean_vs_gauss("bat")
    mean_vs_gauss("cameraman")
    mean_vs_gauss("fog")
    mean_vs_gauss("fognoise")
