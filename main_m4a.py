import whisper
import os
import subprocess

def create_and_open_txt(text, filename):
    # Создаем и записываем текст в файл txt
    with open(filename, "w") as file:
        file.write(text)

    # Открываем файл txt с помощью приложения по умолчанию для txt-файлов
    subprocess.run(["open", filename])

# Запрашиваем у пользователя путь к файлу m4a
path = input("Введите путь к файлу m4a: ")

# Проверяем, что файл существует
if not os.path.isfile(path):
    print("Файл не найден.")
    exit()

# Загружаем модель распознавания речи whisper
model = whisper.load_model("small") #base, small, medium

# Транскрибируем файл и сохраняем результат в переменную result
result = model.transcribe(path, fp16=False)

# Выводим результат на экран и записываем его в файл txt
print(result["text"])
create_and_open_txt(result["text"], "output.txt")
