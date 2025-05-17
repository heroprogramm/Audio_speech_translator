import whisper
import os
from tkinter import filedialog, Tk

# Load Whisper model (you can use 'base', 'small', 'medium', or 'large')
model = whisper.load_model("small")

# Open file picker dialog to select the audio file
root = Tk()
root.withdraw()  # Hide the Tkinter root window
audio_file = filedialog.askopenfilename(title="Select a file", filetypes=[("Audio Files", "*.mp3;*.wav")])

print("You selected:", audio_file)

# Check if a file was selected
if audio_file:
    # Transcribe the audio
    result = model.transcribe(audio_file)
    original_text = result['text']  # Get the transcription text
    print("🗣️ Transcription:", original_text)
else:
    print("No file selected.")
