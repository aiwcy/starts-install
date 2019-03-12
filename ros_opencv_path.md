# ROS 和 OpenCV 在 .zshrc中配冲突

由于.zshrc中opencv路径设置为LD_LIBRARY_PATH=~/opencv3/lib 导致启动ROS时报错，所以将配置opencv的LD_LIBRARY_PATH关闭了，下面附上链接[Answer](https://answers.ros.org/question/67073/roscd-and-roslaunch-problem/) 