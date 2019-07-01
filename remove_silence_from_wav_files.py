import os
from pydub import AudioSegment
import argparse

#得到一秒的静音，属性值为：单通道、16bit、22050Hz
#one_second_silence = AudioSegment.silent(duration=1000, frame_rate=22050)

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms
    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


if __name__ == '__main__':

    #parser = argparse.ArgumentParser(description='Trims a bunch of wav files. From directory: "wav" to a new directory "trimmed-wav"')
    #parser.add_argument('--source', help='Relative path to the dir wavs are at. Default is "wavs"', default='data')
    #parser.add_argument('--destination', help='Relative path to the dir you want your trimmed wavs to be in. Default will create a new dir called "trimmed-wavs"', default='trimmed-wavs')
    #args = parser.parse_args()

    #source_dir = args.source
    #destination_dir = args.destination

    source_dirs = ['E:/FemaleMandarin-1.0-5折交叉验证/group1', 'E:/FemaleMandarin-1.0-5折交叉验证/group2',
                  'E:/FemaleMandarin-1.0-5折交叉验证/group3', 'E:/FemaleMandarin-1.0-5折交叉验证/group4',
                  'E:/FemaleMandarin-1.0-5折交叉验证/group5']

    for source_dir in source_dirs:
        #各源目录对应的输出目录（在源目录后加trim）
        destination_dir = source_dir + 'trim'

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for file in os.listdir(source_dir):
            if file[-4:] != '.wav':
                continue
            current_file_path = os.path.join(source_dir, file)
            file_export_path = os.path.join(destination_dir, file)

            file_stats = os.stat(current_file_path)

            if file_stats.st_size is 0:
                continue

            sound = AudioSegment.from_file(current_file_path, format='wav')
            #开始的毫秒数
            start_trim = detect_leading_silence(sound)
            # 反向开始的毫秒数
            end_trim = detect_leading_silence(sound.reverse())
            duration = len(sound)
            #去首尾静音
            trimmed_sound = sound[start_trim:duration - end_trim]
            #在音频尾部添加1秒的静音
            #trimmed_sound = trimmed_sound + one_second_silence
            #输出音频
            trimmed_sound.export(file_export_path, format='wav')

