# 安装zsh，切换bsh
## 1.安装zsh--shell
- centos: sudo yum install -y zsh
- ubuntu: sudo apt-get install -y zsh
- mac : mac系统自带zsh，如果想安装最新的。brew install zsh

## 2.将系统默认shell更改为zsh
为 root 用户设置 zsh 为系统默认 shell：chsh -s /bin/zsh root
如果你要重新恢复到 bash：chsh -s /bin/bash root

## 3.安装oh_my_zsh
* 如果没有git要先安装git
> - centos: sudo yum install -y git
> - ubuntu: sudo apt-get install -y git
> - mac : brew install git

* 安装oh_my_zsh
> - wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh

## 4.更改主题
* 备份已有的zshrc, 替换zshrc


```
cp ~/.zshrc ~/.zshrc.orig

cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

```

* 配置主题, 可以通过修改~/.zshrc中的环境变量ZSH_THEME来完成

``` ZSH_THEME="agnoster" # (this is one of the fancy ones) 
```

* 修改之后需要重新加载一下

source ~/.zshrc

## 5.使用技巧

- ctrl+r: 快速清屏，mac是command+r
- 连按两次Tab会列出所有的补全列表并直接开始选择，补全项可以使用 ctrl+n/p/f/b上下左右切换
- 在当前目录下输入 .. 或 ... ，或直接输入当前目录名都可以跳转，你甚至不再需要输入 cd 命令了。在你知道路径的情况下，比如 /usr/local/bin 你可以输入 cd /u/l/b 然后按进行补全快速输入
- 命令参数补全。键入 kill <tab> 就会列出所有的进程名和对应的进程号
- 更智能的历史命令。在用或者方向上键查找历史命令时，zsh支持限制查找。比如，输入ls,然后再按方向上键，则只会查找用过的ls命令。而此时使用则会仍然按之前的方式查找，忽略 ls
- 多个终端会话共享历史记录







