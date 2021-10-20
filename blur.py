"""
File: blur.py
Name:黃稚程 mike
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: image, which is the original image
    :return: image, which has been edited
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = new_img.get_pixel(x, y)
            total_red = 0
            total_green = 0
            total_blue = 0
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x + i
                    pixel_y = y +j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            total_red += pixel.red
                            total_green += pixel.green
                            total_blue += pixel.blue
                            count += 1
            new_pixel.red = total_red / count
            new_pixel.green = total_green / count
            new_pixel.blue = total_blue / count
    return new_img


def main():
    """
    This function will blur the original picture.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(15):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
