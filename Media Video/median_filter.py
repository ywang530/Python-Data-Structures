import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

def salt_pepper(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def median_filter(img, kernel_size = 3):
    image = np.zeros((len(img),len(img[0])))
    height, width = image.shape
    # print(height, width)
    window = [0] * (kernel_size * kernel_size)
    offset = kernel_size // 2
    # loop through the image
    for i in range(offset, height - offset):
        for j in range(offset, width - offset):
            idx = 0
            # loop through the window
            for x in range(kernel_size):    
                for y in range(kernel_size):
                    window[idx] = img[i + x - offset][j + y - offset]
                    idx = idx + 1
            # sort the window
            window.sort()
            # find median
            image[i][j] = window[len(window)//2]

    return image


if __name__ == '__main__':
    image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.figure()
    plt.imshow(image, cmap="gray")

    noise = salt_pepper(image, 0.02)
    plt.figure()
    plt.imshow(noise, cmap="gray")

    filtered = median_filter(noise, 3)
    plt.figure()
    plt.imshow(filtered, cmap="gray")

    plt.show()
