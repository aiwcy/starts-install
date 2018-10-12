# 速腾聚创算法组安装软件列表
**说明**
以下介绍的必装软件中部分软件在公司的软件仓库中有（路径是 smb://sti-dl/deeplearningoflidar/Software， 新人可能没有进入的权限，请咨询企业导师 ），例如CUDA、钉钉、HP打印机驱动等，如果没有，请自行下载安装。

**注意** 
下表中没有提及的软件，请勿随意自行安装，安装前最好咨询下企业导师或其它老同事. 

**关于系统更新**
linux与windows系统不同，它是一个开源的系统，Linux的核心理念是“一切皆文件”，整个系统中各个软件包的维护和依赖是松散的，没有一个统一的维护，所以系统更新很可能会造成软件的依赖树被破坏，造成某些包的错误和系统错误。所以，**千万不要随意更新系统！** 对于从windows下迁移过来的新同事，如果你有更新追新的癖好，请打住。建议安装完下列必备软件后请更改系统更新设置：在System Settings->SoftWare & Updates->Updates中，将更新选项改为never或者最长的提醒间隔。如果系统自动弹出更新提醒，请直接关闭即可。

## Ubuntu 软件安装机制

Ubuntu下软件包的安装管理主要有两种：

- apt-get

可以用于安装、卸载、修复性安装、更新系统软件源列表，更新系统等功能，请自行google其命令使用细节。该安装方式属于在线安装方式，原理是从软件源列表中找到对应的软件源服务器地址，自动下载对应安装包并安装。常用功能是：
（1）安装软件：sudo apt-get install xxx（软件包名）
（2）卸载软件：sudo apt-get remove --purge（可选命令，表示彻底卸载，包括配置文件等） xxx（软件包名）
（3）修复安装：sudo apt-get -f install （常用于安装某个软件包时依赖项缺失时自动补全依赖项安装）
（4）更新软件源列表： sudo apt-get update （通常在添加软件源后需要重载时使用）
**注意千万不要轻易使用如下两条指令**
```
sudo apt-get autoremove #系统按照依赖树自动卸载不需要的软件包，可能造成误删软件包！
sudo apt-get upgrade #系统更新命令，Linux系统更新会破坏现有系统的依赖配置，造成系统错乱崩溃，千万不要追新！ 
```


- dpkg

属于离线安装方式，首先需要下载得到安装文件，通常是“.deb”格式，然后常用的安装和卸载命令：
（1）安装软件： sudo dpkg -i xxx.deb
（2）卸载软件： sudo dpkg -r xxx.deb
其它常用命令细节请自行google查询。

除了以上两种主流的软件包安装管理方式外，还有一些小众的安装方式，例如.run文件，这些安装方法和window下的类似，先下载安装文件，然后点击运行安装。**不过要注意的是，Linux权限管理比较严格，可能需要先改变文件的权限才可以运行，更改文件权限命令是：chmod +x xxx（文件名）**。具体的关于chmod命令，请自行查询学习。

## 必装软件
- ROS（Ubuntu 16.04下对应于Kinetic，Ubuntu 14.04 对应于Indigo）
请参照官方wiki进行： http://wiki.ros.org/kinetic/Installation/Ubuntu ，安装并配置系统环境。**ROS安装完成后，会自动安装好OpenCV、PCL、Boost、Eigen等，不需要再重复安装上述包，容易造成系统库配置错乱找不到库的错误**;

- 显卡驱动
切勿按照网上教程自己下载驱动然后安装，容易出问题，现在新版的Ubuntu系统已经集成了驱动管理和安装工具，通过System Settings->SoftWare & Updates->Additional Drivers 切换安装；

- CUDA 9.0 + cuDNN 7.1.3
安装CUDA时不要选择安装显卡驱动和OpenGL，容易出故障，参照前一条单独安装显卡驱动，然后再安装CUDA，最后安装cuDNN；

- Clion

- 代码编辑器vscode或者Atom等
从官网下载deb安装包然后使用dpkg工具安装：
```
sudo dpkg -i xxx.deb
```

- terminator 命令行窗口管理器
```
sudo apt-get install terminator
```
- markdown 编辑器（例如remarkble等）

- 版本管理控制工具git 
```
sudo apt-get install git
```
- 文本编辑器vim （可能系统已经默认安装）

- 钉钉（第三方Linux版本，deb安装包）

- Foxit Reader
官网下载.run安装文件，注意需要对.run文件chmod + X xxx.run才能运行；

- 搜狗输入法
请参照官方给出的安装教程 https://pinyin.sogou.com/linux/help.php

- libpcap pcap文件解析工具
从官网 http://www.tcpdump.org/ 下载source文件， 安装依赖项:
```
sudo apt-get install flex bison byacc -y
```
解压下载的文件 (例如默认下载在 ~/Downloads/目录下), 然后:
```
cd ~/Downloads/libpcap
./configure
make
sudo make install
```
- wireshark UDP抓包工具
```
sudo apt-get install wireshark
```

## 选装软件
- Google Chrome 浏览器
- WPS office办公套装
- 有道词典
- Xpad桌面便签或者Indicator Stickynotes
- Meld文本比较工具
- PyCharm python IDE
- VScode 代码编辑器
- Systemback系统备份还原工具
- HP打印机驱动（用于使用公司局域网打印机）（可选）
参照官网教程安装配置；
- Lantern（蓝灯，VPN翻墙工具）
请通过github安装 https://github.com/getlantern/lantern ，有很多冒牌货；
- htop可视化系统资源进程查看器
- doxygen自动代码注释生成工具
```
sudo apt-get install doxygen
```
- build-essential 系统
```
sudo apt-get install build-essential
```

