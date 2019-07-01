from pydub import AudioSegment
import glob

total_duration = 0
for file in glob.glob(r'E:/FemaleMandarin-1.0-5折交叉验证/group5/*.wav'):
    sound = AudioSegment.from_file(file.replace('\\','/'))
    total_duration += (len(sound) / 1000)

print('音频一共 ' + str(total_duration / 3600) + ' 小时')
