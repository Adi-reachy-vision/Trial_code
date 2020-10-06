import numpy as np
import cv2
import skimage
from skimage.measure import compare_ssim
import matplotlib.pyplot as plt


def mse(imageA, imageB):    #finding the MSE between 2 images
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)    #adding the difference of the square of the images
    err /= float(imageA.shape[0] * imageA.shape[1])     #dividing the sum with the number of pixels in imageA

    return err


def compare_images(imageA, imageB, title):
    imageB = cv2.resize(imageB, (imageA.shape[1], imageA.shape[0]))     # resizing the image to match the 2 images
    m = mse(imageA, imageB)     #performing an MSE comparison between the 2 images
    s = compare_ssim(imageA, imageB)    #comparing the 2 images using SSIM

    fig = plt.figure(title)  #setting the title of the output figure
    s = s[0]  #the output of SSIm has a similrity index and an array value component
    plt.suptitle("MSE: %.2f, MSE: %.2f" % (m, s))   #adding a subtitle
    print(m, s)

    ax = fig.add_subplot(1, 2, 1)   #the first figure
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    ax = fig.add_subplot(1, 2, 2)   #the 2nd figure
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    plt.show()


def main():
    original = cv2.imread("IMG_20201002_134015 (copy).jpg")     #reading the images
    other_image = cv2.imread("IMG_20201002_134015.jpg")
    another_image = cv2.imread("/home/adi/Desktop/cup_whitish_newangle.jpg")

    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)       #converting to grayscale for comparison
    other_image = cv2.cvtColor(other_image, cv2.COLOR_BGR2GRAY)
    another_image = cv2.cvtColor(another_image, cv2.COLOR_BGR2GRAY)

    compare_images(original, original, "Image 1 vs Image 1")    #comparing images
    compare_images(original, other_image, "Image 1 vs Image 2")
    compare_images(original, another_image, "Image 1 vs Image 3")


if __name__ == '__main__':
    main()
