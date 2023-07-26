import whisper
import os
import subprocess
from moviepy.editor import *


def create_and_open_txt(text, filename):
    with open(filename, "w") as file:
        file.write(text)
    subprocess.run(["open", filename])

# Задаем путь к локальному MP4-файлу
local_video_path = input("Введите путь к MP4-файлу на вашем компьютере: ")

# Извлекаем аудио из MP4-файла и сохраняем его в формате MP3
video = VideoFileClip(local_video_path)
output_path = "Youtubeaudios"
filename = "audio.mp3"
video.audio.write_audiofile(os.path.join(output_path, filename))

print(f"Аудио извлечено и сохранено в {output_path}/{filename}")

model = whisper.load_model("small") #base, small, medium
result = model.transcribe(os.path.join(output_path, filename), fp16=False)
print(result["text"])

create_and_open_txt(result["text"], 'output.txt')
