# 语音识别数据集生成

本项目以新闻联播视频为例。

## 下载视频

下载新闻联播视频方式：Windowns或Mac平台的[央视影音](http://app.cctv.com/appkhdxz/pc/index.shtml)软件

下载新闻联播文字稿方式：[新闻联播文字稿](http://www.xwlbo.com/txt.html)。

## 从视频中提取音频

Mac 安装FFmpeg：`brew install ffmpeg`；其它平台请编译[官网](http://www.ffmpeg.org/download.html)下载的压缩包。

运行`Video2Audio.py`。

## 以语音为依据分割音频

运行`segment.py`，使用方法请见文件头注释。

## 语音识别

### 百度

`pip3 install baidu-aip`

运行`os_test.py`

### 讯飞

直接上传至在线识别
