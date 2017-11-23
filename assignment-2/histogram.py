import cv2
import numpy as np

IMAGES_FOLDER = "images"
OUTPUT_FOLDER = "result/original_hist"


def get_histogram(img):
    """
    Construct the histogram of an image
    :param img: the image to get the histogram of
    :return: the histogram as a frequence array of length 256
    """
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


def plot_data(img, out_path):
    """
    Plot histogram and cumulative histogram of a given image
    :param img_file: The path to the image file
    :param out_file: The name to the output file
    :return: None
    """
    f = get_histogram(img)
    cum_f = get_cumulative(f)
    plot = np.zeros((512, 1024))
    add_vals(plot, f, 80)
    add_vals(plot, cum_f, 120)
    cv2.imwrite(out_path, plot)


def original_path(name):
    return "{}/{}.png".format(IMAGES_FOLDER, name)


def original_out_path(name):
    return "{}/{}.png".format(OUTPUT_FOLDER, name)

if __name__ == '__main__':
    plot_data(cv2.imread(original_path("cameraman"), 0), original_out_path("cameraman"))
    plot_data(cv2.imread(original_path("bat"), 0), original_out_path("bat"))
    plot_data(cv2.imread(original_path("fog"), 0), original_out_path("fog"))
    plot_data(cv2.imread(original_path("fognoise"), 0), original_out_path("fognoise"))
