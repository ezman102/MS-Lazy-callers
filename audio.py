import pyaudio
import numpy as np

def detect_specific_sound(duration=3, threshold=1000):
    """Detects sound over a threshold for a specified duration."""
    chunk_size = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    print("Listening for specific sound...")
    try:
        loud_chunks = 0
        while True:
            data = np.frombuffer(stream.read(chunk_size), dtype=np.int16)
            loudness = np.average(np.abs(data))
            if loudness > threshold:
                loud_chunks += 1
                if loud_chunks >= (rate / chunk_size) * duration:
                    print("Specific sound detected.")
                    return True
            else:
                loud_chunks = 0
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
