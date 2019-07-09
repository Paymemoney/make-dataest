import re
import os
# import asr_baidu
from aip import AipSpeech

#####调用百度asr接口进行语音识别
""" 你的 APPID AK SK """
APP_ID = '16698298'
API_KEY = 'fZcfZ0dWXDjvamlhjUkS5DZk'
SECRET_KEY = 'f844dBBNP6N1Yz4aLxCC0lQx7PvSot8g'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


rootdir = './Voice/wavs/' #切成的wav所在目录
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
doc = open(rootdir + 'result.txt', 'w')
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])    # path中保存的是绝对地址
    # print(path)
    # print(path[-3:])
    relatepath = path[len(rootdir)+1:]      # 保存的是相对rootdir的地址
    # print(relatepath)
    if relatepath[-3:] == 'wav':            # 判断是否为wav文件
        # print(relatepath[0:-4])
        result = client.asr(get_file_content(path), 'wav', 16000, {'dev_pid': 1536,})
        
        print(relatepath[0:-4]+':'+result['result'][0])
        print(relatepath[0:-4]+':'+result['result'][0],file=doc)
        # print(':',file=doc)
        
        
doc.close()
