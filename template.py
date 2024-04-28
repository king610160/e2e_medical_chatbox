import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"
]

for filePath in list_of_files:
    fp = Path(filePath)
    # divide the path into folder, and file
    filedir, filename = os.path.split(fp)
    
    # if there is no filedir
    if filedir != '':
        # its makedirs...
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory; {filedir} for the file {filename}')

    # if there is no this file, or the file size is 0, then write the file and log
    if (not os.path.exists(fp)) or (os.path.getsize(filename) == 0):
        with open(fp, 'w') as f:
            pass
        logging.info(f'Creating empty file: {fp}')
    else:
        logging.info(f'{filename} is already existed')
