import os

from modules import script_callbacks

from scripts.utils.settings import get_option
from scripts.utils.eagle_utils import eagle_api, get_folder_id
from scripts.utils.webui_utils import infotext, deepbooru_tags, generater_parameter_tags
from scripts.utils.utils import basename, fullpath, data_url_from_filepath

def on_image_saved(params: script_callbacks.ImageSaveParams):
    if not get_option('enable'): return

    path = fullpath(params.filename)
    name = basename(params.filename)

    annotation = infotext(params.pnginfo)

    tags = deepbooru_tags(params.image) if get_option('enable_deepbooru_tags') else []
    tags = generater_parameter_tags(get_option('generation_parameters'), annotation) + tags

    folder_id = get_folder_id(get_option('save_folder_name_or_id'), get_option('cache_eagle_folder_id'))

    url = data_url_from_filepath(path)
    eagle_api().add_from_url(
        url=url,
        name=name,
        annotation=annotation,
        tags=tags,
        folderId=folder_id
    )

    if get_option('delete_original_files'): os.remove(path)

script_callbacks.on_image_saved(on_image_saved)
