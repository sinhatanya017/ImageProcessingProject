import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):                         #Function to get data about the font depending on the mode
    font = ImageFont.load_default()
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Choosing Background color as Black or White
#bg = "black"
bg = "white"
if bg == "white":
    bg_code = (255, 255, 255)
elif bg == "black":
    bg_code = (0, 0, 0)

char_list, font, scale = get_data("complex")        #Choosing Complex Character list
num_chars = len(char_list)
num_cols = 300

path = "../images/Lenna_(test_image).png"       #Path for the input image

image = cv2.imread(path)

#print(image)

height, width, _ = image.shape

cellWidth = width / num_cols
cellHeight = scale * cellWidth
noOfRows = int(height / cellHeight)

# Calculating Height and Width of the output Image
characterWidth, characterHeight = font.getsize("A")
outputImageWidth = characterWidth * num_cols
outputImageHeight = scale * characterHeight * noOfRows

outputImage = Image.new("RGB", (outputImageWidth, outputImageHeight), bg_code)
draw = ImageDraw.Draw(outputImage)


### Code for printing color Ascii image of the input image


for i in range(noOfRows):
    for j in range(num_cols):
        partial_image = image[int(i * cellHeight):min(int((i + 1) * cellHeight), height), int(j * cellWidth):min(int((j + 1) * cellWidth), width), :]
        partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (cellHeight * cellWidth)
        partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
        c = char_list[min(int(np.mean(partial_image) * num_chars / 255), num_chars - 1)]
        draw.text((j * characterWidth, i * characterHeight), c, fill=partial_avg_color, font=font)
if bg == "white":
    cropImage = ImageOps.invert(outputImage).getbbox()
elif bg == "black":
    cropImage = outputImage.getbbox()

outputImage = outputImage.crop(cropImage)
outputImage.save("../images/output1.jpg")

