import os
import re
import shutil
from pathlib import Path

def organize_files_by_date(directory):
    # Регулярний вираз для пошуку дати у форматі `рік-місяць-день`
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

    # Підбір файлів у папці
    for filename in os.listdir(directory):
        match = date_pattern.search(filename)
        if match:
            date_str = match.group(0)
            date_folder = os.path.join(directory, date_str)
            os.makedirs(date_folder, exist_ok=True)
            source_file = os.path.join(directory, filename)
            destination_file = os.path.join(date_folder, filename)
            shutil.move(source_file, destination_file)
            print(f'Moved {filename} to {date_folder}')

if __name__ == "__main__":
    current_directory = Path().resolve()
    organize_files_by_date(current_directory)
