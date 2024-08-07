import assemblyai as aai
from credentials import secret_api_key_2
aai.settings.api_key = secret_api_key_2


FILE_URL = "C:/Users/nimit/Downloads/the-freesound-blog-community-update-december-2019-57877.mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Error: {transcript.error}")
else:
    
    transcription_text = transcript.text
    print(f"Transcription: {transcription_text}")

    
    with open("transcription.txt", "w") as text_file:
        text_file.write(transcription_text)



