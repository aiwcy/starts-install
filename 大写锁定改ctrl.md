 Ubuntu16.04下修改ctrl caps键位

打开配置文件。

sudo emacs /etc/default/keyboard

找到“XKBOPTIONS”，

交换Capts Lock 与 Control键

XKBOPTIONS="ctrl:swapcaps"

或者设置Caps Lock为Control键

XKBOPTIONS="ctrl:nocaps"

最后执行 sudodpkg-reconfigure keyboard-configuration
