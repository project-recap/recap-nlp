import os
import glob
import skimage.io as io
import pytesseract

from utils import imshow

# Load data
data_path = 'data/biology-campbell/images'
data = glob.glob(data_path + '/ch2*')
data.sort()
imgs = [io.imread(os.path.abspath(img)) for img in data]

pytesseract.image_to_data(imgs[0])
imshow(imgs[0])
