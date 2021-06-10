from PIL import ImageOps
from utils import pdf_to_images, save_images
import glob

# TODO: Use C++ for this, way too slow

# Load Images
textbook_path = 'data/biology-campbell'
chapter = 'ch2'
pdf = textbook_path + '/pdf/{}.pdf'.format(chapter)
imgs = pdf_to_images(pdf)

# Preprocess
imgs = [ImageOps.grayscale(img) for img in imgs]

save_images(imgs, textbook_path + '/images', prefix=chapter)
