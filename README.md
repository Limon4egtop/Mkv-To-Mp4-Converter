# Mkv-To-Mp4-Converter
Python script that will convert any mkv file to mp4

## This script require ffmpeg
There are different ways to install it

### Linux
- Ubuntu & Debian: execute 'sudo apt install ffmpeg'
- Arch: execute 'sudo pacman -S ffmpeg'

### Windows
In Windows you will need to download the ffmpeg.exe
You can download it here: https://github.com/BtbN/FFmpeg-Builds/releases  
Download any releases and find the ffmpeg.exe  
Once you get it you have 2 options
- Add ffmpeg.exe to your PATH
- Copy the .exe into the same folder that the script

### macOS
On macOS, you can install FFmpeg using Homebrew. Follow these steps:

1. If Homebrew is not installed, install it by running the following command in the terminal:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Once Homebrew is installed, install FFmpeg by running:
   ```bash
   brew install ffmpeg
   ```
3. Verify the installation by running:
   ```bash
   ffmpeg -version
   ```
   If FFmpeg is installed correctly, this command will display the installed version and details.

Now you're ready to use the script!







# Конвертер Mkv в Mp4
Python-скрипт для конвертации любого файла MKV в MP4

## Для работы скрипта требуется FFmpeg
Существует несколько способов установки

### Linux
- Ubuntu и Debian: выполните `sudo apt install ffmpeg`
- Arch: выполните `sudo pacman -S ffmpeg`

### Windows
В Windows необходимо скачать ffmpeg.exe
Вы можете загрузить его здесь: https://github.com/BtbN/FFmpeg-Builds/releases  
Скачайте любую версию и найдите ffmpeg.exe  
После этого у вас есть два варианта:
- Добавьте ffmpeg.exe в PATH
- Скопируйте .exe в ту же папку, где находится скрипт

### macOS
На macOS можно установить FFmpeg с помощью Homebrew. Выполните следующие шаги:

1. Если Homebrew ещё не установлен, установите его, выполнив следующую команду в терминале:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. После установки Homebrew установите FFmpeg командой:
   ```bash
   brew install ffmpeg
   ```
3. Проверьте установку, выполнив:
   ```bash
   ffmpeg -version
   ```
   Если FFmpeg установлен корректно, эта команда отобразит информацию о версии и настройках.

Теперь вы готовы использовать скрипт!

