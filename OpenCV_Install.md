# 安装多版本OpenCV

## 下载
到官网下载对应版本，然后解压到根目录

## 编译

cd 到文件中，新建build文件夹， 在build下新建installed文件夹。将文件安装到installed中方便管理。

```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_TBB=ON -D WITH_V4L=ON -D CMAKE_INSTALL_PREFIX=/home/wcy/opencv-2.3.13.4/build/installed .. 
```
其中“CMAKE_INSTALL_PREFIX=”是安装的路径，注意“..”别忘了

## 执行
```
sudo make -j8
```

## 安装
```
sudo make install
```