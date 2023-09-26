import numpy as np
from scipy.io.wavfile import write

# Load an image (you can use any image file)
image = np.array(Image.open('input_image.jpg').convert('L'))

# Normalize the image values to the range [0, 1]
image = image / 255.0

# Define audio parameters
sample_rate = 44100  # Samples per second
duration = 5  # seconds

# Create a time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Create an audio signal by mapping image intensity to amplitude
amplitude = image.ravel()
audio_signal = 0.5 * np.sin(2 * np.pi * 440 * t) * amplitude  # 440 Hz sine wave (adjust as needed)

# Scale audio_signal to the range [-32768, 32767] for 16-bit PCM
audio_signal = np.int16(audio_signal * 32767)

# Save the audio as a WAV file
write('output_sound.wav', sample_rate, audio_signal)