#ubuntu16.04 安装网易云音乐
1. 首先去官网下载最新的网易云

```sudo dpkg -i netease-cloud-music_1.1.0_amd64_ubuntu.deb```

2. 会出现依赖问题，执行以下命令

```sudo apt-get -f install```

3. 启动要用sudo启动，否则可能出现Local file:""("netease-cloud-music")

```sudo nerease-cloud-music```
