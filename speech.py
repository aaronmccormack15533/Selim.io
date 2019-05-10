#!/usr/bin/python3
import speech_recognition as SR

r = SR.Recognizer()

# with SR.Microphone(device_index=1) as source:
#     print('Say Something')
#     r.pause_threshold = 1
#     r.adjust_for_ambient_noise(source, duration=1)
#     audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio)
#         print('you said: {}' .format(text))
#     except:
#         print('could not pick up')

with SR.Microphone() as source:
    print('say something test')
    audio = r.listen(source)
    print('done')

try:
    print("text: " + r.recognize_google(audio))
except Exception as e:
    print(e)

# import pyaudio
# import wave

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()