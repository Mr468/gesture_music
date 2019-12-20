# coding:utf-8
# file: PlayWav.py.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/12/19 12:40
# @desc:播放wav

import pyaudio
import wave
import time


def play_audio_callback(wave_path):
    """
    wav语音文件的播放函数
    :param wave_path:文件路径
    """
    wf = wave.open(wave_path, 'rb')

    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return data, pyaudio.paContinue

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # read data
    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()
