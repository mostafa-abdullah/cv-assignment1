import cv2
import numpy as np

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result"


def get_histogram(image_path):
    """
    Construct the histogram of an image
    :param image_path: the path to the image file
    :return: the histogram as a frequence array of length 256
    """
    img = cv2.imread(image_path, 0)
    histogram = np.zeros(256, int)
    for i in range(len(img)):
        for j in range(len(img[i])):
            histogram[img[i][j]] += 1
    return histogram


def get_cumulative(histogram):
    """
    Get the cumulative frequency of a given histogram
    :param histogram: the histogram to get the cum frequency for
    :return: the cumulative frequency
    """
    return np.cumsum(histogram)


def add_vals(plot, arr, inten):
    """
    Add histogram values to a plot image
    :param plot: The image on which the histogram is displayed
    :param arr: The values of the histogram
    :param inten: The intensity of the histogram
    :return: None
    """
    max_val = arr.max()
    for i, val in enumerate(arr):
        for j in range(0, int((val + 1) / max_val * 512)):
            plot[511 - j][i * 4] += inten
            plot[511 - j][i * 4 + 1] += inten


def plot_data(f, img_file):
    """
    Plot histogram and cumulative histogram
    :param f: The histogram
    :param img_file: The name of the image file
    :return: None
    """
    cum_f = get_cumulative(f)
    plot = np.zeros((512, 1024))
    add_vals(plot, f, 80)
    add_vals(plot, cum_f, 120)
    cv2.imwrite("{}/{}".format(OUTPUT_FOLDER, img_file), plot)


def solve_for_image(img_file):
    hist = get_histogram("{}/{}".format(IMAGES_FOLDER, img_file))
    plot_data(hist, img_file)

solve_for_image("cameraman.png")
solve_for_image("bat.png")
solve_for_image("fog.png")
solve_for_image("fognoise.png")