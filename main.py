# This script transcribes audio from the MP3 file, generates a summary with OpenAI, and saves it in a Word document.
# Ensure an MP3 file is saved in the specified root folder path before running this script.

import openai   # For interacting with OpenAI's API
import os       # For interacting with the operating system
import whisper  # For speech recognition
import docx     # For working with Microsoft Word documents

def check_audio_file_presence(audio_file_path):
    return os.path.exists(audio_file_path)

# Setup your OpenAI API key
def setup_openai_api():
    openai.api_key = "YOUR_API_KEY"

# Transcribe audio using Whisper
def transcribe_audio_with_whisper(audio_file_path):
    print(" 🎙️  Transcribing audio...")
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file_path)
        return result['text']
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

# Save summary to a Word document
def save_summary_to_word(summary, filename="Meeting_Minutes.docx"):
    print(" 💾  Saving summary to Word document...")
    try:
        doc = docx.Document()
        doc.add_paragraph(summary)
        doc.save(filename)
        print(f"Document saved as {filename}. Opening document...")
        os.startfile(filename)  # Automatically opens the file after saving
    except Exception as e:
        print(f"Error saving summary to Word document: {e}")

# Generate summary using OpenAI API
def generate_summary_with_openai(transcription):
    print(" 🤖  Generating summary using OpenAI...")
    try:
        # Read the custom prompt from the prompt.txt file
        with open('prompt.txt', 'r', encoding='utf-8') as file:
            custom_prompt = file.read()
        
        # Adjusting the API call to use the chat completions endpoint with the custom prompt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specifying the chat model
            messages=[
                {'role': 'system', 'content': custom_prompt},
                {'role': 'user', 'content': transcription}
            ],
            max_tokens=1024
        )
        # Extracting the response text from the chat completion
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error during summary generation with OpenAI: {e}")
        return "Summary generation failed."
    

# Main execution function
def process_meeting_minutes(audio_file_path):
    if not check_audio_file_presence(audio_file_path):
        print("  ⚠️  Please save the mp3 file in the root folder before running.")
        return
    setup_openai_api()
    transcription = transcribe_audio_with_whisper(audio_file_path)
    if transcription:
        print("Transcription complete.")
        summary = generate_summary_with_openai(transcription)
        save_summary_to_word(summary)
        print(" 📋  Process completed. The meeting minutes have been saved in a Word document.")
    else:
        print(" ❌  Transcription failed, no text to process.")

# File path for the audio file
audio_file_path = r'C:\..path_to_your_audio_file\audio.mp3'
process_meeting_minutes(audio_file_path)
