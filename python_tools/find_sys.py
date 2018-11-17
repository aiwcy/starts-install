import os
from PIL import Image


def find_sys(source_dir, target_dir):

    for j in range(1, 4000):
        vole = []
        for file in os.listdir(source_dir):
            a = len(file)
            if int(file[2:a-4]) == j:
                vole.append(file)
        if len(vole) > 1:
            for file1 in vole:
                name = target_dir + file1
                im = Image.open(source_dir + file1)
                im.save(name)

#if __name__ == __main__:
source_dir = "/home/cywang/Download/calibration-toolbox-0.9/data/data-jpg/"
target_dir = "/home/cywang/Download/calibration-toolbox-0.9/data/tmp/"
find_sys(source_dir, target_dir)






