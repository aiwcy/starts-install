from glob import glob
from PIL import Image
import os
import math

def resize_images(source_dir, target_dir, threshold):
#def resize_images(source_dir, target_dir):
    filenames = glob('{}/*'.format(source_dir))
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for filename in filenames:
        filesize = os.path.getsize(filename)
        if filesize >= threshold:
            print(filename)
            with Image.open(filename) as im:

                width, height = im.size
                if width >= height:
                    new_width = int(width/2.0)
                    new_height = int(height/2.0)
                else:
                    new_height = int(width/2.0)
                    new_width = int(height/2.0)

                resized_im = im.resize((new_width, new_height))
                output_filename = filename.replace(source_dir,target_dir )
                output_filename = filename.replace('jpeg', 'jpg')
                resized_im.save(output_filename)

if __name__ =='__main__':
    source_dir = "/home/cywang/Download/calibration-toolbox-0.9/data/data1/"
    target_dir = "/home/cywang/Download/calibration-toolbox-0.9/data/data-jpg/"
    resize_images(source_dir,target_dir,409600)
