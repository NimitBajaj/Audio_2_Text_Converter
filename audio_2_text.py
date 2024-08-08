import assemblyai as aai
from credentials import secret_api_key_2
from tkinter import *
from tkinter import filedialog, messagebox
import os

aai.settings.api_key = secret_api_key_2



def convert_to_text():
    file_path=entry.get()
    

    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(file_path)
        

        if transcript.status == aai.TranscriptStatus.error:
            print(f"Error: {transcript.error}")
        else:
    
            transcription_text = transcript.text
            print(f"Transcription: {transcription_text}")

            transcription_file_path = os.path.join(os.getcwd(), "transcription.txt")
            with open("transcription.txt", "w") as text_file:
               text_file.write(transcription_text)
               messagebox.showinfo("Success", f"Transcription saved as {transcription_file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3")])
    if file_path:
        entry.delete(0, END)
        entry.insert(0, file_path)

root=Tk()
root.title("Audio to Text Converter")

frame=Frame(root,padx=20, pady=20)
frame.pack(padx=10, pady=10)

label=Label(frame, text="Select Audio Files:")
label.grid(row=0, column=0, sticky=W)

entry=Entry(frame, width=50)
entry.grid(row=0, column=1, pady=5)

browse_button=Button(frame, text="Browse", command= browse_file)
browse_button.grid(row=0, column=2, padx=5)

convert_button=Button(frame, text="Convert to Text", command=convert_to_text)
convert_button.grid(row=1, columnspan=5, padx=5)

root.mainloop()
    