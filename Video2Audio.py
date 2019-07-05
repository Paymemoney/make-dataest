from pydub import AudioSegment
import os
import sys


def convert_video(source_path, target_path):
    mp3_filename = os.path.splitext(os.path.basename(source_path))[0] + '.mp3'
    target = target_path + "/" + mp3_filename
    AudioSegment.from_file(source_path).export(target, format='mp3')


source_path = "/Users/scirocco/SRTP/Video/" # must end with '/'
target_path = "/Users/scirocco/SRTP/Voice"
for root, dirs, files in os.walk(source_path):
    for file in files:
        convert_video(source_path + file, target_path)
