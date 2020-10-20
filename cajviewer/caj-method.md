# ubuntu 安装caj文件阅读器
- Ctrl+Alt+t 打开命令终端
- 安装wine软件 ： sudo apt-get install wine 
- 下载CAJViewer安装包 ：[http://pan.baidu.com/s/1mhwEvAK]( http://pan.baidu.com/s/1mhwEvAK)
- 安装rar格式解压缩命令 ： sudo apt-get install unrar
- 新建cajviewer文件夹并把CAJViewer安装包解压缩  ：
 ```sudo mkdir cajviewer```  
 ```  sudo unrar x CAJViewer6.0_green.rar.park cajviewer```
 - 进入cajviewer文件夹修改CAJViewer.exe程序权限 ：
 ```cd cajviewer```
 ```sudo chmod u+x CAJViewer.exe```
 在wine下运行cajViewer.exe程序 ：
 ```wine CAJViewer.exe ```