# Ubuntu 安装 MATLAB方法
##挂载映像文件
1. 把所需文件都拷贝到了home目录，用完就删，反正硬盘有备份。在/home/wcy/ 下新建文件夹matlab用来当做挂载点
```
mkdir ~/matlab
```

 挂载第一个盘
```
sudo mount -t auto -o loop R2018a_glnxa64_dvd1.iso  ~/matlab
```
##安装MATLAB

1. 挂载iso之后，会发现文件系统多了一个盘，说明挂载成功，然后进行安装：
```
sudo ./matlab/install
```
 进行安装，然后选择使用文件安装秘钥，不需要Internet链接，然后下一步下一步，将readme里面第一个秘钥粘贴上去，一只默认，然后点击安装。
 
 2.  安装进行到60%的时候，会弹出一个提示框，说请插入dvd2，这时候我们需要重新开一个终端，把dvd2挂载到matlab文件夹中：
```
sudo mount -t auto -o loop R2018a_glnxa64_dvd1.iso  ~/matlab/
```
3. 然后在对话框中点击OK，继续安装。完成安装后取消iso挂载：
```
$ umount matlab/
$ sudo rm -r matlab/ # 删除空的文件夹
```
## 激活Matlab
1. 安装完成后，可以在终端中输入matlab打开软件，如果失败，只能去安装位置打开：
```
$ cd /usr/local/MATLAB/R2016b/bin
$ ./matlab # 如果是第一次运行，建议加sudo
```
第一步，先载入激活文件license_standalone.lic： 
第二步，把Crack文件夹下面的/R2018a/bin/glnxa64/matlab_startup_plugins/lmgrimpl/libmwlmgrimpl.so 拷到/usr/local/MATLAB/R2018a/bin/glnxa64/matlab_startup_plugins/lmgrimpl/里面。
##建立软连接（快捷启动）
```
sudo ln -s /usr/local/MATLAB/R2018a/bin/matlab /usr/local/bin/matlab
```
##参考网址
安装：https://blog.csdn.net/Jesse_Mx/article/details/53956358
软连接：https://blog.csdn.net/will_ye/article/details/79573399