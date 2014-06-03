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

def out_or_in(out_or_in, img):
    if "out" in out_or_in:
        raw_img = img.convert("RGB")
        inverted_image = PIL.ImageOps.invert(raw_img)
        inverted_image = inverted_image.convert("1")
        inverted_image.save("img.png")
    elif "in" in out_or_in:
        img.save("img.png")
    else:
        "try again"
        out_or_in = raw_input("out or in?")
        out_or_in_method(out_or_in, img)


out_or_in = raw_input("Do you want the black part out or in?")
qr_code_string = raw_input("What is your text?")
border_size = int(raw_input("How big of a border do you want?"))

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
#img = Image.open("test/test.png")
#A = imread("test/test.png") 
#rsize = img.resize((img.size[0]/10,img.size[1]/10))
#rsizeArray = np.asarray(rsize)

A = imread("img.png") * 256
# You still need to larn what the line below does
#A = A[:, :, 0] + 1.*A[: ,:, 2] # Compose RGBA channels to give depth
# Default min_thickness_percent = 1.5
# Default scale .05
length_width = float(raw_input("how many mm^2 do you want the qr code to be?"))
# .2 corresponds to about 1 cm
height = float(raw_input("what %age of the length do you want to be the height / depth of the black bit?"))
base_percentage = float(raw_input("what % do you want the base to take up?"))
numpy2stl(A, "qr.stl", scale=height, mask_val=0.0, solid=True, 
        min_thickness_percent=base_percentage, max_width=length_width, 
        max_depth=length_width)
#image2stl test/test.png -scale 0.04 -mask_val .0 -RGBA_weights 1. 0. 1. 0. -gaussian_filter .0
