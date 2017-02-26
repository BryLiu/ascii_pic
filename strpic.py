#encoding:utf-8
from PIL import Image
import sys

ascii_chars = ['-', 's', 'c', '.', ':', ';', '[', '+', '%', '#', '@']
# [ '#', 'a', '%', '?', '.', '+', '@', '*', '$', ',', 'x']

#resize the picture
def scale_image(im,new_width=100):
    original_width,original_height = im.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(original_height * aspect_ratio)
    return im.resize((new_width,new_height))

#change the picture mode
def turn2gray(im):
    return im.convert('L')

#map
def map_pixels2char(im,range_width=25):
    """The gray level is 0-255,divide into 11,each get 25"""
    pic_pixels = list(im.getdata())
    pixels2char = [ascii_chars[pixel_value/range_width]for pixel_value in pic_pixels]
    return ''.join(pixels2char)

def convert_pic(im,new_width = 100):
    im = scale_image(im)
    im = turn2gray(im)
    pixels2char = map_pixels2char(im)
    length_pic_char = len(map_pixels2char(im))
    ascii_pic = [pixels2char[index:index+new_width] for index in xrange(0,length_pic_char,new_width)]
    return '\n'.join(ascii_pic)

def handle_pic_transfer(file_path):
    try:
        im = Image.open(filePath)
    except IOError:
        print "could not open the image file"
        return
    image_ascii= convert_pic(im)
    print image_ascii
if __name__ == '__main__':
    filePath = sys.argv[1]
    handle_pic_transfer(filePath)