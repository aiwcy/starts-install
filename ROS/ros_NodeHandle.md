# ROS NodeHandle笔记
## ros::NodeHandle::param()
该函数是从param服务器中获取参数值给变量.如果无法获取，则将默认值赋给变量。这个函数的功能和getParam()函数类似，区别是param()函数还提供了一个默认值。