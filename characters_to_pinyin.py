from pypinyin import pinyin, Style
import glob
import re

#pinyin with tone : pin1 yin1
def character_to_TONE3(filepath):
    out = ''
    with open(filepath, 'r', encoding='utf-8') as f:
        input = f.readline()
        # 将THCHS-30中文中的空格去掉再进行汉字转拼音
        input = re.sub('\s+', '', input)

    str = pinyin(input, style = Style.TONE3)
    for row in str:
        for line in row:
            out = out + line + ' '
    with open(filepath, 'a', encoding='utf-8') as f:
        out = out.strip()
        f.write('\n' + out)

#pinyin with tone : pi1n yi1n
def character_to_TONE2(filepath):
    out = ''
    with open(filepath, 'r', encoding='utf-8') as f:
        input = f.readline()
        # 将THCHS-30中文中的空格去掉再进行汉字转拼音
        input = re.sub('\s+', '', input)

    str = pinyin(input, style = Style.TONE2)
    for row in str:
        for line in row:
            out = out + line + ' '
    with open(filepath, 'a', encoding='utf-8') as f:
        out = out.strip()
        f.write('\n' + out)

# pinyin without tone : pin yin
def character_to_NORMAL(filepath):
    out = ''
    with open(filepath, 'r', encoding='utf-8') as f:
        input = f.readline()
        #将THCHS-30中文中的空格去掉再进行汉字转拼音
        input = re.sub('\s+', '', input)

    str = pinyin(input, style = Style.NORMAL)
    for row in str:
        for line in row:
            out = out + line + ' '
    with open(filepath, 'a', encoding='utf-8') as f:
        out = out.strip()
        f.write('\n' + out)

trn_files = []
trn_files += glob.glob('E:/thchs30_去燥_去静音_A6_3折交叉验证/data_6/group1/*.trn')
trn_files += glob.glob('E:/thchs30_去燥_去静音_A6_3折交叉验证/data_6/group2/*.trn')
trn_files += glob.glob('E:/thchs30_去燥_去静音_A6_3折交叉验证/data_6/group3/*.trn')
trn_files += glob.glob('E:/thchs30_去燥_去静音_A6_3折交叉验证/data_30.61/*.trn')
trn_files += glob.glob('E:/thchs30_去燥_去静音_A6_3折交叉验证/data_30.61_augmentation/*.trn')
trn_files += glob.glob('E:/thchs30_去燥_去静音_A6_3折交叉验证/noise(A5 A9)/*.trn')
trn_files += glob.glob('E:/thchs30_去燥_去静音_A6_3折交叉验证/6号原始发音文件备份/*.trn')

for trn in trn_files:
    #character_to_TONE3(trn)
    character_to_TONE2(trn)
    character_to_NORMAL(trn)
