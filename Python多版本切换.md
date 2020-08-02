update-alternatives是Debian提供的一个工具(非Debian系的就不用看了)，原理类似于上面一个办法，也是通过链接的方式，但是其切换的过程非常方便。
#首先我们先看一下有没有关于Python的可选项：
1.$ update-alternatives --display python
update-alternatives: 错误: 无 python 的候选项
#那首先先建立python的组,并添加Python2和Python3的可选项

2.$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2 # 添加Python2可选项，优先级为2
3.$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1 #添加Python3可选项，优先级为1

注意，这里的 /usr/bin/python 链接文件，两个可选项必须是一样的，这样这个链接文件才可以选择两个不同的可选项去链接。

这时如果我们查看 /usr/bin/python 这个文件时，会发现它已经链接到了 /etc/alternatives/python 。

然后我们再看一下版本
$ python --version
Python 2.7.6

为什么还是Python2，看一下配置
$ sudo update-alternatives --config python
有 2 个候选项可用于替换 python (提供 /usr/bin/python)。
选择 路径 优先级 状态

    0 /usr/bin/python2.7 2 自动模式
    1 /usr/bin/python2.7 2 手动模式
    2 /usr/bin/python3.4 1 手动模式
    要维持当前值[*]请按回车键，或者键入选择的编号：

原来是因为默认选中了自动模式，而Python2的优先级高于Python3，（如果选择0，默认自动模式，会使用python2.7,如果选择1选择手动模式，Python2的优先级高于Python3，选择Python2,），这时候只要键入2,就可以使用Python3了。

如果你想要删除某个可选项的话：

$ sudo update-alternatives --remove python /usr/bin/python2.7
update-alternatives只适用于Debian系Liunx
