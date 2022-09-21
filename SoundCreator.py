import math
import wave
import struct

class GridSpace:
    def __init__(self):
        self.audio_x = []
        self.audio_y = []
        self.sample_rate = 44100.0

    def append_sine(self, freq_x, freq_y):
        num_samples = 500 * (self.sample_rate / 1000.0)
        for x in range(int(num_samples)):
            self.audio_x.append(math.sin(2 * math.pi * freq_x * ( x / self.sample_rate )))
            self.audio_y.append(math.sin(2 * math.pi * freq_y * ( x / self.sample_rate )))
        return

    def save_wave(self):
        nframes = len(self.audio_x)
        wav_file=wave.open("nbc.wav","w")
        wav_file.setparams((2, 2, self.sample_rate, nframes, "NONE", "not compressed"))

        for s, t in zip(self.audio_x, self.audio_y):
            wav_file.writeframes(struct.pack('h', int( s * 32767.0 )))
            wav_file.writeframes(struct.pack('h', int( t * 32767.0 )))
        wav_file.close()
        return

if __name__ == "__main__":
    gs = GridSpace()
    gs.append_sine(freq_x = 227.9, freq_y=200)
    gs.append_sine(freq_x = 329.6, freq_y=360)
    gs.append_sine(freq_x = 261.6, freq_y=250)
    gs.save_wave()