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

- 存在多版本OpenCV时，需要找到所需版本对应的OpenCVConfig.cmake文件，并将其路径添加到工程的CMakeLists.txt中。
示例如下：

```
 
 cmake_minimum_required(VERSION 2.8)
 
 set(OpenCV_DIR "~/opencv-3.4.1/build")
 
 project(test)
 
 find_package(OpenCV REQUIRED)

```
