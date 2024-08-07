#import openai
#from credentials import secret_api_key
#openai.api_key= secret_api_key
#audio_path="C:/Users/nimit/Downloads/the-freesound-blog-community-update-december-2019-57877.mp3"
#audio_file=open(audio_path,"rb")
#response=openai.Audio.translate("whisper-1",audio_file)
#print(response)

#import openai
#from credentials import secret_api_key

#openai.api_key = secret_api_key
#audio_path = "C:/Users/nimit/Downloads/the-freesound-blog-community-update-december-2019-57877.mp3"

#with open(audio_path, "rb") as audio_file:
#    response = openai.Audio.transcribe(
#        model="whisper-1",
#        file=audio_file
#    )

#print(response['text'])

import assemblyai as aai
from credentials import secret_api_key_2
aai.settings.api_key = secret_api_key_2


FILE_URL = "C:/Users/nimit/Downloads/the-freesound-blog-community-update-december-2019-57877.mp3"



transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)




