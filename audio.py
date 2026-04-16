import pyaudio
p = pyaudio.PyAudio()


stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,          # mic
    output=True,         # speakers
    frames_per_buffer=1024
)

data = stream.read(1024)
stream.write(data)




p.terminate()