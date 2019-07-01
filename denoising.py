import numpy as np
import matplotlib.pyplot as plt
import os
import wave
import librosa
import soundfile as sf
from time import time

def denoising_file(in_filename, out_filename):
    # 打开语音文件。
    f = wave.open(in_filename, 'rb')
    # 得到语音参数
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = f.readframes(nframes)
    waveData = np.fromstring(strData, dtype=np.short)
    # 归一化
    waveData = waveData * 1.0 / max(abs(waveData))
    # 将音频信号规整乘每行一路通道信号的格式，即该矩阵一行为一个通道的采样点，共nchannels行
    wav = (np.reshape(waveData, [nframes, nchannels]).T)[0]  # .T 表示转置
    f.close()  # 关闭文件
    duration = len(wav) / framerate
    print('采样点总数：' + str(len(wav)))
    print("采样率：" + str(framerate))
    print('总时长：' + str(duration))

    framelength = 0.025  # 帧长20~30ms
    framesize = framelength * framerate  # 每帧点数 N = t*fs,通常情况下值 为256或512,要与NFFT相等\
    # 而NFFT最好取2的整数次方,即framesize最好取的整数次方

    # 找到与当前framesize最接近的2的正整数次方
    nfftdict = {}
    lists = [32, 64, 128, 256, 512, 1024]
    for i in lists:
        nfftdict[i] = abs(framesize - i)
    sortlist = sorted(nfftdict.items(), key=lambda x: x[1])  # 按与当前framesize差值升序排列
    framesize = int(sortlist[0][0])  # 取最接近当前framesize的那个2的正整数次方值为新的framesize

    NFFT = framesize  # NFFT必须与时域的点数framsize相等，即不补零的FFT
    overlapSize = 1.0 / 3 * framesize  # 重叠部分采样点数overlapSize约为每帧点数的1/3~1/2
    overlapSize = int(round(overlapSize))  # 取整
    frame_shift_size = framesize - overlapSize
    print("帧长为{},帧叠为{},帧移为{},傅里叶变换点数为{}".format(framesize, overlapSize, frame_shift_size,  NFFT))
    spectrum, freqs, ts, fig = plt.specgram(wav, NFFT=NFFT, Fs=framerate, window=np.hanning(M=framesize),
                                            noverlap=overlapSize, mode='default', scale_by_freq=True, sides='default',
                                            scale='dB', xextent=None)  # 绘制频谱图
    spectrum_T = spectrum.T
    print('频谱图shape： ' + str(spectrum.shape))
    frame = 1
    for row in spectrum_T:
        # if not row.all() and frame > int(round(framerate / frame_shift_size)):
        if row.all() == 0 and frame > int(round(framerate / frame_shift_size)):
            print('从第 ' + str(frame + 2) + ' 帧处开始截断')
            break
        frame += 1

    end_point = (frame + 2) * frame_shift_size + 1
    sf.write(out_filename, wav[: end_point], framerate)

def denoising_files(in_directory, out_directory):
    out = ''
    for file in os.listdir(in_directory):
        if file.endswith('wav'):
            start = time()
            denoising_file(os.path.join(in_directory, file), os.path.join(out_directory, file))
            out = out + str((time() - start)) + '\n'
            print('花费 ' + str((time() - start)) + '秒')
            print('##########################')
    with open(os.path.join(out_directory, 'time.txt'), 'w', encoding = 'utf-8') as fw:
        out = out.strip()
        fw.write(out)

def main():
    denoising_files('E:/test', 'E:/test')


if __name__ == "__main__":
    main()