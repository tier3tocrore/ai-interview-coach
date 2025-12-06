from faster_whisper import WhisperModel
import moviepy.editor as mp
import os

# Load model (cached for speed)
@st.cache_resource
def load_whisper_model():
    return WhisperModel("large-v3", device="cpu", compute_type="int8")

model = load_whisper_model()

def transcribe_video(video_path):
    # Extract audio
    clip = mp.VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    clip.audio.write_audiofile(audio_path, logger=None)
    
    # Transcribe (auto-detects Hindi/English)
    segments, info = model.transcribe(audio_path, beam_size=5, language=None)
    
    full_text = " ".join([segment.text.strip() for segment in segments])
    
    # Cleanup
    clip.close()
    os.unlink(audio_path)
    
    return full_text
