import librosa
import scipy
import numpy as np
from PIL import Image

def spectogram(file_path, stride_ms = 10.0, window_ms = 20.0, max_freq = None, eps = 1e-14):
    samples, sample_rate = librosa.load(file_path)
    stride_size = int(0.001 * sample_rate * stride_ms)
    window_size = int(0.001 * sample_rate * window_ms)

    # Extract strided windows
    truncate_size = (len(samples) - window_size) % stride_size
    samples = samples[:len(samples) - truncate_size]
    nshape = (window_size, (len(samples) - window_size) // stride_size + 1)
    nstrides = (samples.strides[0], samples.strides[0] * stride_size)
    windows = np.lib.stride_tricks.as_strided(samples, 
                                          shape = nshape, strides = nstrides)

    assert np.all(windows[:, 1] == samples[stride_size:(stride_size + window_size)])

    # Window weighting, squared Fast Fourier Transform (fft), scaling
    weighting = np.hanning(window_size)[:, None]

    fft = np.fft.rfft(windows * weighting, axis=0)
    fft = np.absolute(fft)
    fft = fft2

    scale = np.sum(weighting2) * sample_rate
    fft[1:-1, :] *= (2.0 / scale)
    fft[(0, -1), :] /= scale

    # Prepare fft frequency list
    freqs = float(sample_rate) / window_size * np.arange(fft.shape[0])

    # Compute spectrogram feature
    ind = np.where(freqs <= max_freq)[0][-1] + 1
    spec = np.log(fft[:ind, :] + eps)
    img = Image.fromarray(spec, 'RGB')
    img.save('spectogram.jpg')
    return img.show()
file_path = r"C:\Users\anshu\Desktop\cool_sound.wav"
spectogram(file_path, max_freq = 30000)