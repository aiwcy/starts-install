# 创建catkin_ws工作空间出现catkin_make错误解决方法

## 错误代码： 
The specified base path “/home/ubuntu/catkin_ws” contains a CMakeLists.txt but “catkin_make” must be invoked in the root of workspace…..

## 出现这种情况的原因是catkin_init_workspacce的时候，出现下面这句： 
Creating symlink “/home/ubuntu/catkin_ws/CMakeLists.txt” pointing to “/opt/ros/indigo/share/catkin/cmake/toplevel.cmake”

将当前工作空间下的CMakeLists.txt与/ros/下的cmake做了链接

## 解决方法： 
unlink /home/ubuntu/catkin_ws/CMakeLists.txt 
