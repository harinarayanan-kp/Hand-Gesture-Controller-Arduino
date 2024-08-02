import numpy as np
import pyaudio
import struct
import serial

# Initialize serial connection with Arduino
com_port = 'COM6'  # Adjust COM port accordingly
baud_rate = 9600
ser = serial.Serial(com_port, baud_rate)

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Thresholds for mapping audio intensity to finger counts
thresholds = [500, 1000, 2000, 3000, 4000]  # Adjust according to your audio input

def send_command(finger_counts):
    command = ''.join(map(str, finger_counts)) + '\n'
    ser.write(command.encode())

def process_audio(data):
    # Convert binary data to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)
    # Perform FFT (Fast Fourier Transform) on the audio data
    fft_data = np.fft.fft(audio_data)
    # Calculate the magnitudes of the frequencies
    magnitude = np.abs(fft_data)
    # Take average magnitude to represent overall intensity
    intensity = np.mean(magnitude)
    # Scale intensity to finger counts (assuming 5 fingers)
    finger_counts = [1 if intensity > threshold else 0 for threshold in thresholds]
    return finger_counts

while True:
    # Read audio from microphone
    data = stream.read(CHUNK)
    
    # Process audio data to get finger counts
    finger_counts = process_audio(data)
    print("Finger count from audio:", finger_counts)
    send_command(finger_counts)

# Release resources
stream.stop_stream()
stream.close()
p.terminate()
