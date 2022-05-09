import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('1.jpg')
edges = cv2.Canny(img,100,100)

kernel = np.ones((9, 9))
# do a morphologic close
res = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

c = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(c)

# draw the biggest contour (c) in green
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

result = np.zeros_like(img)
cv2.drawContours(result, [c], 0, (255,255,255), cv2.FILLED)

for contour in contours:
    convexHull = cv2.convexHull(contour)
    cv2.drawContours(img, [convexHull], -1, (255, 0, 0), 2)

proj = np.zeros((img.shape[0],img.shape[1],3))
h = proj.shape[0]
w = proj.shape[1]

countArr = []
count = 0
# loop over the image, pixel by pixel
for y in range(0, h):
    for x in range(0, w):
        if result[y, x][0] == 255 and result[y, x][1] == 255 and result[y, x][2] == 255:
            count = count + 1
    countArr.append(count)
    count = 0

print(countArr)
print(len(countArr))
print(h)

for y in range(0, len(countArr)):
    for x in range(0, countArr[y]):
        proj[y, x][0] = 255
        proj[y, x][1] = 255
        proj[y, x][2] = 255

cv2.imshow('original', img)
cv2.imshow('edged', edges)
cv2.imshow('connected', res)
cv2.imshow('result', result)
cv2.imshow('proj', proj)



cv2.waitKey(0)

