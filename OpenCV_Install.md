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

##opencv3.3和opencv_contrib的编译安装
https://blog.csdn.net/xiangxianghehe/article/details/78780269
##编译安装过程中的问题
在编译过程中会出现类似于下面的问题
```
The imported target "Qt5::Gui" references the file "/usr/lib/x86_64-linux-gnu/libEGL.so" but this file does not exist.
```
解决办法：
```
$ ls /usr/lib/x86_64-linux-gnu | grep -i libegl
libEGL.so 
libEGL.so.1 
libEGL.so.346.59

$ ls -l /usr/lib/x86_64-linux-gnu/libEGL.so
lrwxrwxrwx 1 root root 18 mar 30 17:10 /usr/lib/x86_64-linux-gnu/libEGL.so -> mesa-egl/libEGL.so
```
或者cd到该目录下找到该文件，在zsh下面可以看到该文件是红色，可能是链接坏了，需要重新创建链接
```
sudo rm /usr/lib/x86_64-linux-gnu/libEGL.so
sudo ln /usr/lib/x86_64-linux-gnu/libEGL.so.1 /usr/lib/x86_64-linux-gnu/libEGL.so
```