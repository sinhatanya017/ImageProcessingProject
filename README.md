# Image Processing Project using OpenCV and Pillow

Opencv is an open source library which is very useful for computer vision applications.
OpenCV can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects etc.

This project uses OpenCV two implent the two functionalities present in it.
The first one being generation of ASCII Art of any input image and the other one being a virtual Paint.

## Internal Working

1. ASCII Art Generator-
This feature works on the concatenation of string. In this feature , we take an input image, choose a background color, either black or white, and then concatenate in a string characters of matching luminosity, using two loops, one for the rows and nested inside it another for columns.
Then after cropping the image accordingly, it's printed in an output window.

2. Virtual Paint-
This feature uses the color identifying property of OpenCV and uses it to make a Virtual Paint environment. In this feature , we initialize the colors that we want to get identified and being used as a brush. Then we use their HSV properties to identify the contours of the specified colors if prompted on the screen.Then we start reading the video from our image detecting source, in this came my laptop's webcam. Now as soon as the the required color is prompted on the screen, the program starts detecting it's contours and points on the tip and stores them in an array, which will act as the tip of the brush.

## Learning from the Project

This project helped me in understanding basic as well as some advanced functions of OpenCV and Pillow and implementing them in interesting projects .
This project helped me in understanding the perception of image by a machine and it's manipulation.

## Demo

Insert gif or link to demo

## Resources used

1. https://analyticsindiamag.com/how-to-create-a-virtual-painting-app-using-opencv/
2. https://towardsdatascience.com/tutorial-webcam-paint-opencv-dbe356ab5d6c
3. https://www.geeksforgeeks.org/converting-image-ascii-image-python/
