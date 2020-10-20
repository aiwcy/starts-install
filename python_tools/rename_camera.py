import os

path = '/home/cywang/Download/calibration-toolbox-0.9/data/camera4_sync'
for file in os.listdir(path):
    if file[-4:] == 'jpeg':
        name = file.replace('4-', '')
        newname = '5-'+name
        os.rename(os.path.join(path, file), os.path.join(path, newname))
