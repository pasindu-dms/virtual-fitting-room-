import cv2
import numpy as np
import os
import glob
from scipy import ndimage

color_codes = {
    "red": [0, 0, 255],
    "yellow": [0, 255, 255],
    "green":   [0, 128, 0],
    "purple":  [128, 0, 128],
    "orange":  [0, 165, 255],
    "pink":    [203, 192, 255],
    "deeppink": [147, 20, 255],
    "blue":  [255, 0, 0],
    "brown":  [42, 42, 165],
    "white": (255, 255, 255),
    "black":  [0, 0, 0],
    "magenta":  [255, 0, 255],
    "violet":   [238, 130, 238],
    "lavender": [250, 230, 230]
}

def return_color_code(color):
    return color_codes[color]


def select_image(input):
    img_path = ''
    if input["type"] == "shirt":
        img_path = "shirt3.png"
    elif input["type"] == "frock":
        img_path = "frock.jpg"

    binarize_image(input, img_path)

def binarize_image(input,img_path):
    img = cv2.pyrDown(cv2.imread(img_path, cv2.IMREAD_UNCHANGED))
    # print(img.ndim)

    # img = cv2.resize(img, (900, 900), 0, 0, cv2.INTER_LINEAR)
    ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 25, 255, cv2.THRESH_BINARY)
    # thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # kernel = np.ones((5, 5), np.uint8)
    # eroded = cv2.erode(threshed_img, kernel, iterations=1)

    cv2.imshow('original', img)
    cv2.imshow('binarized', threshed_img)

    selectDress(input, img, threshed_img)

def selectDress(input, original, binarized_img):
    if input["type"] == "shirt":
        drawShirt(input, original, binarized_img)
    elif input["type"] == "frock":
        drawFrock(input, original, binarized_img)


# def paintImage(original, binarized):
#     contours, hierarchy = cv2.findContours(binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     # print(len(contours))
#     # cv2.drawContours(original, contours[4], -1, (0, 255, 0), 3)
#     cv2.fillPoly(original, pts=[contours[2]], color=(255, 0, 0))
#     cv2.fillPoly(original, pts=[contours[3]], color=(255, 0, 0))
#     cv2.fillPoly(original, pts=[contours[4]], color=(255, 0, 0))
#     cv2.fillPoly(original, pts=[contours[5]], color=(255, 0, 0))
#
#     # print(cv2.contourArea(contours[5]))
#     cv2.imshow('countours', original)
#     cv2.waitKey(0)

def drawShirt(input, original, binarized):
    contours, hierarchy = cv2.findContours(binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    collar_contours = [6, 7]
    sleev_contours = [2, 3]
    body_contours = [4,5]

    if input["collar"]:
        for cont in collar_contours:
            cv2.fillPoly(original, pts=[contours[cont]], color=return_color_code(input["collar"]["color"]))
    if input["sleev"]:
        for cont in sleev_contours:
            cv2.fillPoly(original, pts=[contours[cont]], color=return_color_code(input["sleev"]["color"]))

    for cont in body_contours:
        cv2.fillPoly(original, pts=[contours[cont]], color=return_color_code(input["color"]))

    cv2.imshow('countours', original)
    cv2.waitKey(0)

def drawFrock(input, original, binarized):
    contours, hierarchy = cv2.findContours(binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    top_contours = 5
    middle_contour = 4
    bottom_contours = 3
    underline_contour = 2
    collar_contour = 6

    if input["collar"]:
        cv2.fillPoly(original, pts=[contours[collar_contour]], color=return_color_code(input["collar"]["color"]))

    if input["bottom"]:
        cv2.fillPoly(original, pts=[contours[bottom_contours]], color=return_color_code(input["bottom"]["color"]))

    if input["top"]:
        cv2.fillPoly(original, pts=[contours[top_contours]], color=return_color_code(input["top"]["color"]))

    cv2.imshow('countours', original)
    cv2.waitKey(0)



input_shirt = {
    "type": "shirt",
    "color": "green",
    "collar": {"color": "red"},
    "sleev": {"color": "orange"}
}

input_frock = {
    "type": "frock",
    "top": {"color": "green"},
    "bottom": {"color": "red"},
    "collar": {"color": "red"}
}


select_image(input_frock)