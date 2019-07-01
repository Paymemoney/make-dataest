from aip import AipSpeech

#####调用百度asr接口进行语音识别
""" 你的 APPID AK SK """
APP_ID = '10639705'
API_KEY = '7GUxgxM2srEL6QnYfW40SuVW'
SECRET_KEY = '96fe7cda08421cdcaa4f875d4a7b33bd'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



print(client.asr(get_file_content('E:/biaobei-1.0/wavs/000004.wav'), 'wav', 16000, {'dev_pid': 1536,})['result'][0])
