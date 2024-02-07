import time
from functools import lru_cache

from scripts.utils.eagle_api import EagleAPI
from scripts.utils.settings import get_option

def eagle_api() -> EagleAPI:
    return EagleAPI(get_option('endpoint'), get_option('port'))

def get_folder_id(folder_name_or_id: str | None, enable_cache: bool = False) -> str | None:
    if not folder_name_or_id: return None

    return _get_folder_id(folder_name_or_id, time.time() if not enable_cache else 0)

@lru_cache(maxsize=1)
def _get_folder_id(folder_name_or_id: str, _: float = 0) -> str | None:
    folders = eagle_api().list_folders()
    return find_folder_by_folder_id_or_name(folder_name_or_id, folders)

def find_folder_by_folder_id_or_name(name_or_id: str, folders: list[any]) -> str | None:
    flatten_folders = []
    for item in folders:
        flatten_folders.append(item)
        if "children" in item and item["children"]:
            for child in item["children"]:
                flatten_folders.append(child)

    filtered = sorted(
                    filter(lambda folder: folder['id'] == name_or_id or folder['name'] == name_or_id, flatten_folders),
                    key=lambda folder: folder['modificationTime'],
                    reverse=True
                )

    if filtered:
        return filtered[0].get('id')
    else:
        return None