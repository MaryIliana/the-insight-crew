import os
import re
from typing import Union
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

from flask_uploads import DATA, UploadSet

DOC_DATA = UploadSet("data", DATA)


def save_data(data: FileStorage, folder: str = None, name: str = None ) -> str:
    """Toakes FileStorage and saves it to a folder"""
    return DOC_DATA.save(data, folder, name)

def get_path(filename: str = None, folder: str = None) -> str:
    """Take image name and folder return full path"""
    return DOC_DATA.path(filename, folder)

def find_data_any_format(filename: str, folder: str) -> Union[str, None]:
    """Takes de filename and returns an data on any of the accept formats."""
    for _format in DATA:
        data = f"{filename}.{_format}"
        data_path = DOC_DATA.path(filename=data, folder=folder)
        if os.path.isfile(data_path):
            return data_path
    return None

def _retrieve_filename(file: Union[str, FileStorage]) -> str:
    """Take FileStorage and return the filename.
    Allows our functions to call this with both file names and
    FileStorage and always gets back a file name.
    """
    if isinstance(file, FileStorage):
        return file.filename
    return file

def is_filename_safe(file: Union[str, FileStorage]) -> bool:
    """Check our regex and return whether the string matches or not"""
    filename = _retrieve_filename(file)
    
    allowed_format = "|".join(DATA)
    regex = f"^[a-zA-Z0-9][a-zA-Z0-9_()-\.]*\.({allowed_format})$"
    return re.match(regex, filename) is not None

def get_basename(file: Union[str, FileStorage]) -> str:
    """Return full name of data in the path
    get_basename('some/folder/data.csv') return 'data.csv'
    """
    filename = _retrieve_filename(file)
    return os.path.split(filename)[1]
    
def get_extension(file: Union[str, FileStorage]) -> str:
    """Return file extension
    get_extension('data.csv') return '.csv' 
    """
    filename = _retrieve_filename(file)
    return os.path.splitext(filename)[1]