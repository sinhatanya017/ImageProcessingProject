import cv2
import numpy as np

frame_Width = 640  # Setting Output Frame width
frame_Height = 480  # Setting Output Frame height

cap = cv2.VideoCapture(0)  # Defining a video capture object
                           # Setting value 0 for default camera

cap.set(3, frame_Width)
cap.set(4, frame_Height)
cap.set(10, 150)

# Virtual Painter identifies and paints the following colors-
# Purple
# Green
# Blue
# Yellow


targetColorVals = [[133, 56, 0, 159, 156, 255],     # [Hue Minimum, Saturation Minimum, Value Minimum,
                   [57, 76, 0, 100, 255, 255],      #   Hue Maximum, Saturation Maximum, Value Maximum]
                   [90, 48, 0, 118, 255, 255],
                   [21, 40, 180, 38, 255, 255]]

paintColorVals = [[186, 85, 211],  # BGR code for our paint brush
                  [0, 255, 0],
                  [255, 0, 0],
                  [0, 255, 255]]

points = []  # Array in which identified points will be appended


def detectColor(img, targetColorVals, paintColorVals):      #Function that will detect the color on the input screen
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)           #Converting image from BGR to HSV

    #       H = Hue, S = Saturation, V = Value(relative lightness or darkness of a color)

    cnt = 0
    newPoints = []
    for color in targetColorVals:
        lowerBound = np.array(color[0:3])           #Lower Bound of Hue, Saturation and Value of Colors
        upperBound = np.array(color[3:6])           #Upper Bound of Hue, Saturation and Value of Colors
        mask = cv2.inRange(imgHSV, lowerBound, upperBound)
        x, y = contourFunc(mask)
        cv2.circle(imgResult, (x, y), 7, paintColorVals[cnt], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, cnt])
        cnt += 1
    return newPoints


def contourFunc(img):               #Function to detect the contour of the input object
    contours, order = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def paintFunction(points, paintColorVals):          #Function to paint on the output screen
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 7, paintColorVals[point[2]], cv2.FILLED)
        # cv2.circle(image, center_coordinates, radius, color, thickness)


while True:
    test, img = cap.read()
    imgResult = img.copy()
    newPoints = detectColor(img, targetColorVals, paintColorVals)
    if len(newPoints) != 0:
        for newP in newPoints:
            points.append(newP)
    if len(points) != 0:
        paintFunction(points, paintColorVals)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):                  #Wait key value 1 so that while loop of sequence of images
        break                                              #seems like a video
                                                           #Program will stop running, if key 'q' is pressed
