import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(
    filename="input.wav",
    duration=5,
    sample_rate=16000
):
    print("🎤 Listening...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(
        filename,
        sample_rate,
        recording
    )

    print("✅ Recording complete")

    return filename