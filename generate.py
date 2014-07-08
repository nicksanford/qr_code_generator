#!env/bin/python
# Don't forget to change to your fork of stl_tools
import qrcode
import sys
import PIL
from PIL import Image
import PIL.ImageOps
from scipy.misc import lena
from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl, text2png
import qrcode

def create_qr(qr_code_string, out_or_in, border_size, length_width, height, base_percentage):
    print qr_code_string
    print out_or_in
    print length_width
    print border_size
    print height
    print base_percentage
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            # This will modify the border default 2
            border=border_size,
    )
    qr.add_data(qr_code_string)
    qr.make(fit=True)
    img = qr.make_image()
    out_or_in_method(out_or_in, img)
    A = imread("img.png") * 256

    stl = numpy2stl(A, "qr.stl", scale=height, mask_val=0.0, solid=True, 
            min_thickness_percent=base_percentage, max_width=length_width, 
            max_depth=length_width, max_height=1000)
    return stl

def out_or_in_method(out_or_in, img):
    if out_or_in:
        raw_img = img.convert("RGB")
        inverted_image = PIL.ImageOps.invert(raw_img)
        inverted_image = inverted_image.convert("1")
        inverted_image.save("img.png")
    else:
        img.save("img.png")
     

#out_or_in = raw_input("Do you want the black part out or in?")
#qr_code_string = raw_input("What is your text?")
#border_size = float(raw_input("How big of a border do you want?"))
# Default min_thickness_percent = 1.5
# Default scale .05
#length_width = float(raw_input("how many mm^2 do you want the qr code to be?"))
# .2 corresponds to about 1 cm
#height = float(raw_input("what %age of the length do you want to be the height / depth of the black bit?"))
#base_percentage = float(raw_input("what % do you want the base to take up?"))

#f = open("test.stl", "wb")
#f.write(create_qr(qr_code_string, out_or_in, length_width, border_size, height, base_percentage))
#f.close()
