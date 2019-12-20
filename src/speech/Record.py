# coding:utf-8
# file: Record.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/12/18 12:29
# @desc:录音文件


import pyaudio
import wave

input_filename = "input.wav"  # 麦克风采集的语音输入
input_filepath = "音频存储位置"  # 输入文件的path
in_path = input_filepath + input_filename


class Record(object):

    def __init__(self, speech_view):
        self.speech_view = speech_view

    def get_audio(self, filepath):
        """
        开启麦克风录音
        :param filepath:录音文件存储路径
        """
        self.speech_view = False
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1  # 声道数
        RATE = 16000  # 采样率
        RECORD_SECONDS = 2
        WAVE_OUTPUT_FILENAME = filepath
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        print("*" * 10, "开始录音：请在2秒内输入语音")

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            wf.writeframes(data)
        print("*" * 10, "录音结束\n")

        # wf.writeframes(b''.join(frames))

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()

        # play_audio_callback(filepath)
