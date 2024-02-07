import base64
import os
import mimetypes

from modules import paths

def fullpath(filename: str) -> str:
    return os.path.join(paths.script_path, filename)

def basename(path: str) -> str:
    return os.path.basename(path)

def data_url_from_filepath(path: str) -> str:
    with open(path, "rb") as f:
        encoded = base64.urlsafe_b64encode(f.read()).decode('utf-8')
        url = f"data:{mimetypes.guess_type(path)[0]};base64, {encoded}"

    return url
