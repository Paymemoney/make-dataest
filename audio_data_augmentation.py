from pydub import AudioSegment
import os
import glob
import shutil

def augmentation(file):
    sound = AudioSegment.from_file(file)
    # shift the pitch up by half an octave (speed will increase proportionally)
    octaves = -0.01
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    # keep the same samples but tell the computer they ought to be played at the
    # new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
    chipmunk_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    # now we just convert it to a common sample rate (44.1k - standard audio CD) to
    # make sure it works in regular audio players. Other than potentially losing audio quality (if
    # you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
    chipmunk_ready_to_export = chipmunk_sound.set_frame_rate(22050)
    file = file.replace('\\', '/')
    outdir, filename = os.path.split(file)
    out_path = os.path.join(outdir, filename[:-4] + '_-0.01aug.wav').replace('\\', '/')
    #print(out_path)
    chipmunk_ready_to_export.export(out_path, format='wav')

    # 复制trn文件
    trnfile = (file + '.trn').replace('\\', '/')
    outpath = os.path.join(outdir, trnfile[:-8] + '_-0.01aug.wav.trn').replace('\\', '/')
    shutil.copyfile(trnfile, outpath)



if __name__ == '__main__':
    wav_files = []
    wav_files += glob.glob('E:/FemaleMandarin-1.0-5折交叉验证-去首尾静音/group1/*[0-9].wav')
    wav_files += glob.glob('E:/FemaleMandarin-1.0-5折交叉验证-去首尾静音/group2/*[0-9].wav')
    wav_files += glob.glob('E:/FemaleMandarin-1.0-5折交叉验证-去首尾静音/group3/*[0-9].wav')
    wav_files += glob.glob('E:/FemaleMandarin-1.0-5折交叉验证-去首尾静音/group4/*[0-9].wav')
    wav_files += glob.glob('E:/FemaleMandarin-1.0-5折交叉验证-去首尾静音/group5/*[0-9].wav')
    wav_count = 0
    for file in wav_files:
        augmentation(file)
        wav_count += 1
    print('音频: ' + str(wav_count) + ' 个')










