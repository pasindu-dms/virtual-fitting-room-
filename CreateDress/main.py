import cv2
import numpy as np
import os
import glob
from scipy import ndimage


def binarize_image(img_path):
    img = cv2.pyrDown(cv2.imread(img_path, cv2.IMREAD_UNCHANGED))
    print(img.ndim)

    # img = cv2.resize(img, (900, 900), 0, 0, cv2.INTER_LINEAR)
    ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 25, 255, cv2.THRESH_BINARY)
    # thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # kernel = np.ones((5, 5), np.uint8)
    # eroded = cv2.erode(threshed_img, kernel, iterations=1)

    cv2.imshow('original', img)
    cv2.imshow('binarized', threshed_img)
    # cv2.imshow('eroded', eroded)
    # cv2.waitKey(0)

    drawMinArea(img, threshed_img)

def drawMinArea(original, binarized):
    # find contours and get the external one

    contours, hierarchy = cv2.findContours(binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    # cv2.drawContours(original, contours[4], -1, (0, 255, 0), 3)
    cv2.fillPoly(original, pts=[contours[2]], color=(255, 0, 0))
    cv2.fillPoly(original, pts=[contours[3]], color=(255, 0, 0))
    cv2.fillPoly(original, pts=[contours[4]], color=(255, 0, 0))
    cv2.fillPoly(original, pts=[contours[5]], color=(255, 0, 0))

    print(cv2.contourArea(contours[5]))
    cv2.imshow('countours', original)
    cv2.waitKey(0)

input = {
    "type": "shirt",
    "color": "white",
    "collar": {"color": "red"}
}

binarize_image('shirt3.png')