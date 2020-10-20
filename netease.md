#ubuntu16.04 安装网易云音乐
1. 首先去官网下载最新的网易云
```官网看不到下载16.04的链接，只有18.04，但是依旧可以访问到，地址为：

http://s1.music.126.net/download/pc/netease-cloud-music_1.0.0_amd64_ubuntu16.04.deb```

```sudo dpkg -i netease-cloud-music_1.1.0_amd64_ubuntu.deb```

2. 会出现依赖问题，执行以下命令

```sudo apt-get -f install```

3. 启动要用sudo启动，否则可能出现Local file:""("netease-cloud-music")

```sudo nerease-cloud-music```
