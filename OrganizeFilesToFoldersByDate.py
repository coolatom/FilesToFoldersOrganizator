import os
import re
import shutil
from pathlib import Path

def organize_files_by_date(directory):
    # A regular expression for searching for filenames containing a Date in `year-month-day' format
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

    # View files in a Directory
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
