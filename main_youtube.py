import whisper
from pytube import YouTube
import os
import subprocess


def create_and_open_txt(text, filename):
    # Create and write the text to a txt file
    with open(filename, "w") as file:
        file.write(text)

    # Open the txt file using the default application associated with txt files
    subprocess.run(["open", filename])

# Ask user for the YouTube video URL
url = input ("Enter the YouTube video URL: ")


# Create a YouTube object from the URL
yt = YouTube (url)

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
output_path = "Youtubeaudios"
filename = "audio.mp3"
audio_stream.download(output_path=output_path, filename=filename)

print(f"Audio downloaded to {output_path}/{filename}")

model = whisper.load_model ("base") #base, small, medium
result = model.transcribe("Youtubeaudios/audio.mp3", fp16=False)
print(result["text" ])

create_and_open_txt(result["text"], 'output.txt')


#To update the package to the latest version of this repository, please run:

#pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

# Устанавливаем pip install -U openai-whisper
# далее ставим вот это: brew install ffmpeg
#еще ставим вот это: pip install pytube

#https://github.com/openai/whisper