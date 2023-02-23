# video-bpm-snapshot

随着视频音乐的节拍摇摆吧！

一个图一乐的小玩意，提取音频节拍截取视频帧

### 环境配置

`conda install -c conda-forge aubio`

以及opencv-python

### accuracy

没算过，可以人工标定并给予一个可接受阈值来算，但就是没算

### 局限

目前只允许本地视频process，不能URL

### 后续（潜在）方向

- 提取字幕，生成歌词（因此对于一个二创视频，很轻易可以提取歌词）
- 台词提取器（自动生成可用于训练VITS的dataset）

### Demo

向各位二创作者表示严重的感谢~

1. 我是如何 因为鉴证毁掉自己人生的？（灵感来源）

   https://www.bilibili.com/video/BV12v4y1s7K2

（接下来是夹带私货环节）

2. 【TNO】硅晶之梦 索尼-长实线：漫步人生路

   https://www.bilibili.com/video/BV1ST411d7VQ

3. 【全明星】【文艺复兴】喂之歌

   https://www.bilibili.com/video/BV17x4y157BM

