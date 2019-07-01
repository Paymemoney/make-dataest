import grequests
import logging
import json
from googletrans import Translator
from googletrans.utils import format_json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
translator = Translator(service_urls=['translate.google.cn'])

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='E:/语音识别与中文转英语/log.txt')
logger = logging.getLogger()


def exception_handler(request, exception):
    logger.warning('exception when at %s :%s',request.url,exception)


def work(urls):
    reqs = (grequests.get(u,verify=True, allow_redirects=True, timeout=4) for u in urls)
    res = grequests.map(reqs, exception_handler=exception_handler,size=20)
    return res

def totaltranslate():
    file2 = open('E:/语音识别与中文转英语/cn2en_en.txt',mode='a',encoding='utf-8')

    with open('E:/语音识别与中文转英语/cn.txt',mode='r',encoding='utf-8') as f:
        urls = []
        num = 0
        for line in f:
            num+=1

            line = line.strip()
            token = translator.token_acquirer.do(line)
            url="https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=3&tsel=0&kc=1&tk={0}&q={1}".format(token,line)
            urls.append(url)

            if len(urls) >= 50:
                res = work(urls)
                for r in res:
                    if hasattr(r,'status_code'):
                        if r.status_code == 200:
                            try:
                                a=format_json(r.text)
                                target = ''.join([d[0] if d[0] else '' for d in a[0]])
                                source = ''.join([d[1] if d[1] else '' for d in a[0]])
                            except Exception as e:
                                logger.error('when format:%s',e)
                                logger.error('%s\n%s',r.text)
                                source = ''
                                target = ''
                            if len(source) != 0 and len(target) != 0:
                                file2.write(target+'\n')
                            else:
                                file2.write('\n')
                        else:
                                file2.write('\n')
                urls = []
                logger.info('finish 50 sentence, now at %s',num)
        print(num)
    file2.close()

def sentencetranslate(line):
    line = line.strip()
    text = translator.translate(line,src='zh-cn',dest='en').text
    return text

def completetranslate():
    file1 = open('E:/语音识别与中文转英语/cn2en_en.txt',mode='r',encoding='utf-8')
    file2 = open('E:/语音识别与中文转英语/new_cn2en_en.txt',mode='a',encoding='utf-8')
  #  cn_num_lines = sum(1 for line in open('E:/语音识别与中文转英语/cn.txt',mode='r',encoding='utf-8'))
    en_num_lines = sum(1 for line in open('E:/语音识别与中文转英语/cn2en_en.txt',mode='r',encoding='utf-8'))

    i = 0
    with open('E:/语音识别与中文转英语/cn.txt',mode='r',encoding='utf-8') as f:
        for line in f:
            if(i < en_num_lines):
                t = file1.readline()
                if len(t) == 1:#'only \n'
                    text = sentencetranslate(line)
                    file2.write(text+'\n')
                else:
                    file2.write(t)

            else:
                text = sentencetranslate(line)
                file2.write(text + '\n')
            i += 1

    file1.close()
    file2.close()


if __name__ == "__main__":
    totaltranslate()
    completetranslate()