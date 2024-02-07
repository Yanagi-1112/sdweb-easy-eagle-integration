from modules import script_callbacks, shared, ui_components

GENERATION_PARAMETERS = [
    "Model",
    "Model hash",
    "Sampler",
    "Size",
    "Version",
]

OPTIONS = [
    [
        "enable",
        {
            "default": True,
            "label": "ファイルの保存時に Eagle にもファイルを送信する"
        }
    ],
    [
        "delete_original_files",
        {
            "default": False,
            "label": "Eagle に送信したあとに元のファイルを削除する"
        }
    ],
    [
        "save_folder_name_or_id",
        {
            "default": "",
            "label": "ファイルを保存するフォルダの名前またはID"
        }
    ],
    [
        "enable_deepbooru_tags",
        {
            "default": False,
            "label": "Deepbooru を使用してタグを付ける"
        }
    ],
    [
        "generation_parameters",
        {
            "default": [],
            "label": "タグに追加する生成パラメータ",
            "component": ui_components.DropdownMulti,
            "component_args": lambda: { "choices": GENERATION_PARAMETERS }
        }
    ],
    [
        "cache_eagle_folder_id",
        {
            "default": True,
            "label": "Eagle のフォルダ情報をキャッシュする(かすかに高速化されますが、Eagle 側でのフォルダ名の変更が反映されなくなります)"
        }
    ],
    [
        "endpoint",
        {
            "default": "http://localhost",
            "label": "Eagle のエンドポイントURL"
        }
    ],
    [
        "port",
        {
            "default": 41595,
            "label": "Eagle のポート番号"
        }
    ]
]

def on_ui_settings():
    for option in OPTIONS:
        shared.opts.add_option(
            f"easy_eagle_integration_{option[0]}",
            shared.OptionInfo(
                **option[1],
                section=("easy_eagle_integration", "Easy Eagle Integration"))
            )

def get_option(option_name: str) -> any:
    return getattr(shared.opts, f"easy_eagle_integration_{option_name}")

script_callbacks.on_ui_settings(on_ui_settings)