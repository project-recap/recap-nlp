import os
from pdf2image import convert_from_path
from matplotlib import pyplot as plt

def pdf_to_images(pdf_path):
    data_dir = os.path.abspath(pdf_path)
    return convert_from_path(data_dir)

def save_images(images, save_path, prefix='', ext='.jpg'):
    for i, image in enumerate(images):
        image.save(save_path + '/{}-{}{}'.format(prefix, i, ext))

def imshow(img):
    plt.imshow(img, interpolation='nearest')
    plt.show()
