import math
import struct
import wave
import random

sample_rate = 44100
duration = 2.4 # 2.4 seconds of screaming goat

num_samples = int(sample_rate * duration)
samples = []

# Screaming goat parameters
# It starts with a sudden inhale/shout, screams at high pitch with rapid warble, then tapers off into a raspy bleat

phase1 = 0.0
phase2 = 0.0
phase3 = 0.0
lfo_phase = 0.0

for i in range(num_samples):
    t = i / sample_rate
    
    # Pitch contour: sudden rise, high chaotic plateau, falling bleat
    if t < 0.15:
        # Rapid rise
        pitch = 380 + (t / 0.15) * 380 # rises to 760 Hz
    elif t < 1.4:
        # Climax scream with chaotic pitch variation
        chaos = math.sin(t * 19.0) * 45 + math.sin(t * 37.0) * 25
        pitch = 760 + chaos - (t - 0.15) * 60
    elif t < 1.9:
        # Ragged descent
        pitch = 680 - ((t - 1.4) / 0.5) * 280 + math.sin(t * 24.0) * 50
    else:
        # Dying bleat
        pitch = 400 - ((t - 1.9) / 0.5) * 160 + math.sin(t * 16.0) * 40
        
    # Bleating goat LFO vibrato (16-22 Hz warble)
    vibrato_rate = 16.0 + 6.0 * (t / duration)
    lfo = math.sin(2.0 * math.pi * vibrato_rate * t)
    pitch_mod = pitch + lfo * 45.0
    
    # Phase increments for rich sawtooth/pulse scream
    phase1 += 2.0 * math.pi * pitch_mod / sample_rate
    phase2 += 2.0 * math.pi * (pitch_mod * 1.012) / sample_rate # slight detune
    phase3 += 2.0 * math.pi * (pitch_mod * 0.503) / sample_rate # sub-harmonic throat growl
    
    # Sawtooth waveform with harmonics
    s1 = 2.0 * (phase1 / (2.0 * math.pi) - math.floor(phase1 / (2.0 * math.pi) + 0.5))
    s2 = 2.0 * (phase2 / (2.0 * math.pi) - math.floor(phase2 / (2.0 * math.pi) + 0.5))
    s3 = math.sin(phase3)
    
    # Add throat distortion and breath noise
    noise = (random.random() * 2.0 - 1.0) * 0.18
    raw_scream = 0.55 * s1 + 0.35 * s2 + 0.25 * s3 + noise
    
    # Soft clipping distortion (overdrive human scream)
    clipped = math.tanh(raw_scream * 2.2)
    
    # Amplitude envelope
    if t < 0.05:
        env = t / 0.05
    elif t < 1.5:
        env = 0.95 - (t - 0.05) * 0.1
    elif t < 2.1:
        env = 0.8 - ((t - 1.5) / 0.6) * 0.5
    else:
        env = 0.3 * (1.0 - (t - 2.1) / 0.3)
        
    val = clipped * env * 0.9
    val = max(-1.0, min(1.0, val))
    samples.append(int(val * 32767))

with wave.open("goat_scream.wav", "w") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    for s in samples:
        wav_file.writeframes(struct.pack('<h', s))

print(f"Generated goat_scream.wav successfully ({len(samples)} samples)")
