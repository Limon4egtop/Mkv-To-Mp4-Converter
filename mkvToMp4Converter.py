import os
import ffmpeg  # pip install ffmpeg-python
import sys

# Получить текущую директорию
start_dir = os.getcwd()
input_dir = os.path.join(start_dir, "input")  # Папка input
output_dir = os.path.join(start_dir, "output")  # Папка output

# Убедимся, что папка output существует
os.makedirs(output_dir, exist_ok=True)

# Функция для преобразования файла .mkv в .mp4 (ТРЕБУЕТ НАЛИЧИЯ FFMPEG.EXE В ТОЙ ЖЕ ПАПКЕ, ЧТО И СКРИПТ)
def convert_to_mp4(mkv_file, output_path):
    name, ext = os.path.splitext(os.path.basename(mkv_file))
    out_name = os.path.join(output_path, name + ".mp4")
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Завершено преобразование: {} -> {}".format(mkv_file, out_name))

# Функция для обработки всех файлов .mkv в папке input
def convert_folder_to_mp4():
    # Проверяем, существует ли папка input
    if not os.path.exists(input_dir):
        print("Папка input не найдена. Создайте папку input и добавьте файлы .mkv.")
        return

    # Перебираем файлы в папке input
    for file in os.listdir(input_dir):
        if file.endswith('.mkv'):
            mkv_file = os.path.join(input_dir, file)
            print("Найден файл: {}".format(mkv_file))
            convert_to_mp4(mkv_file, output_dir)
        else:
            print("Пропущен файл: {} (не .mkv)".format(file))

if __name__ == "__main__":
    if len(sys.argv) == 1:  # Если аргументы не переданы, обрабатываем все файлы из input
        print("Все файлы .mkv из папки input будут преобразованы в .mp4 и сохранены в папке output. Нажмите Enter для продолжения.")
        input()
        convert_folder_to_mp4()
    else:  # Если передан конкретный файл, конвертируем только его
        mkv_file = sys.argv[1]
        if os.path.isfile(mkv_file) and mkv_file.endswith('.mkv'):
            print("Передан файл: {}".format(mkv_file))
            print("Нажмите Enter для продолжения.")
            input()
            convert_to_mp4(mkv_file, output_dir)
        else:
            print("Ошибка: Передан файл не формата .mkv или файл не существует.")
