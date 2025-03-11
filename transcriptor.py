import whisper
import noisereduce as nr
import numpy as np
import librosa
import soundfile as sf

def transcribe_with_whisper(audio_file_name, language="auto"):
    try:
        # Load audio and reduce noise
        y, sr = librosa.load(audio_file_name, sr=16000)
        reduced_noise = nr.reduce_noise(y=y, sr=sr)

        # Save denoised audio
        denoised_audio_file = "denoised_" + audio_file_name
        sf.write(denoised_audio_file, reduced_noise, sr)

        # Load Whisper model
        model = whisper.load_model("medium")  # Can use "tiny", "base", "small", "medium", or "large"

        # Transcribe audio
        result = model.transcribe(denoised_audio_file, language=language if language != "auto" else None)
        
        return result["text"]

    except Exception as e:
        return f"❌ Error: Transcription failed. {str(e)}"
