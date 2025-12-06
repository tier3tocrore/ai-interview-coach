import streamlit as st
from transcription import transcribe_video
from utils import detect_fillers
import os
import tempfile

st.set_page_config(page_title="Tier3ToCrore AI Interview Coach", layout="wide", initial_sidebar_state="collapsed")

# Dark theme CSS
st.markdown("""
    <style>
    .main {background-color: #000000;}
    .stApp {background-color: #000000;}
    .stTitle {color: white;}
    .stText {color: white;}
    .stMarkdown {color: white;}
    .stFileUploader {background-color: #1e1e1e;}
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Tier3ToCrore AI Interview Coach")
st.markdown("**From Tier-3 to ₹100 Cr** – Upload your mock video for instant transcript + filler analysis")

uploaded_file = st.file_uploader("Upload Mock Interview Video", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    # Save temp file
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(uploaded_file.read())
    video_path = tfile.name
    tfile.close()

    st.video(video_path)
    
    with st.spinner("Transcribing with Whisper large-v3... (10–30 sec)"):
        transcript = transcribe_video(video_path)
    
    st.subheader("📝 Full Transcript")
    st.write(transcript)
    
    fillers = detect_fillers(transcript)
    st.warning(fillers)
    
    st.download_button("💾 Download Transcript", transcript, file_name="interview_transcript.txt", mime="text/plain")
    
    # Cleanup
    os.unlink(video_path)
