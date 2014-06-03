from scipy.misc import lena
from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl, text2png
import qrcode

#img = Image.open("test/test.png")
#A = imread("test/test.png") #rsize = img.resize((img.size[0]/10,img.size[1]/10))
#rsizeArray = np.asarray(rsize)


A = imread("test/eric_qr_neg.png") * 256
# You still need to larn what the line below does
#A = A[:, :, 0] + 1.*A[: ,:, 2] # Compose RGBA channels to give depth
numpy2stl(A, "test/eric_qr_out.stl", scale=0.05, mask_val=0.0, solid=True, min_thickness_percent=1.5, max_width=40., max_depth=40.)
#image2stl test/test.png -scale 0.04 -mask_val .0 -RGBA_weights 1. 0. 1. 0. -gaussian_filter .0
