#多版本Opencv切换
 - 打开~/.bashrc 或者 ~/.zshrc
 
 在文件末尾增加以下内容
 
 ```
 
  export PKG_CONFIG_PATH=～/opencv-3.4.1/build/installed/lib/pkgconfig
 
  export LD_LIBRARY_PATH=～/opencv-3.4.1/build/installed/lib
 
 ```
 
 - 更新.bashrc 或.zshrc
 
 - 查询Opencv版本
 > ```pkg-config --modversion opencv```
 
 - 如果只有一个版本的OpenCV，在CMakeList.txt中使用以下语句即可。
> ```FIND_PACKAGE(OpenCV REQUIRED)```

>在OpenCV编译好后，所在目录中会生成OpenCVConfig.cmake文件，这个文件中指定了CMake要去哪里找OpenCV，其.h文件在哪里等。

- 不同版本切换的方法：

不同版本的OpenCV编译好后，都会生成一个 OpenCVConfig.cmake，这个文件中指定了对应库函数和头文件的位置。在本教程的情况下，OpenCV2对应的OpenCVConfig.cmake在/usr/local/opencv2/share/OpenCV，OpenCV3对应的OpenCVConfig.cmake在/usr/local/opencv3/share/OpenCV。因此，如果要使用那个版本的OpenCV只需要将对应版本OpenCVConfig.cmake的路径写入CMakeLists.txt即可。这就是说，当自己所写的程序使用到OpenCV3时，在 FIND_PACKAGE( OpenCV REQUIRED ) 前，添加set(OpenCV_DIR “/usr/local/opencv3/share/OpenCV”) 这样计算机就找到OpenCV3的对应头文件和库文件了，如果使用OpenCV2，那么添加set(OpenCV_DIR “/usr/local/opencv2/share/OpenCV”)在FIND_PACKAGE( OpenCV REQUIRED ) 前就好。比如下面是一个使用OpenCV3的例子。

```
 
CMAKE_MINIMUM_REQUIRED( VERSION 2.8)

PROJECT(useOpenCV)

set(OpenCV_DIR "/usr/local/opencv3/share/OpenCV") 

FIND_PACKAGE(OpenCV REQUIRED)

INCLUDE_DIRECTORIES(${OpenCV_INCLUDE_DIRS})

add_executable(useOpenCV useOpenCV.cpp)

TARGET_LINK_LIBRARIES(useOpenCV ${OpenCV_LIBRARIES})

```
#网址：https://blog.csdn.net/u011092188/article/details/77842002
