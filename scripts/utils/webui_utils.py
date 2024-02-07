from modules import deepbooru, infotext_utils

def infotext(pnginfo: dict) -> str:
    parameters = pnginfo.get('parameters', "")
    extras = pnginfo.get("extras", None)

    if extras:
        return parameters + '\n' + extras
    else:
        return parameters

def deepbooru_tags(image):
    deepbooru.model.start()
    booru = deepbooru.model.tag_multi(image, force_disable_ranks=True)
    deepbooru.model.stop()

    tags = [ x.strip() for x in booru.split(",") if x.strip() != "" ]

    return tags

def generater_parameter_tags(generation_parameters: list[str], infotext: str):
    gen_params = infotext_utils.parse_generation_parameters(infotext)
    gen_params_tags = list(filter(lambda x: x[1] is not None, map(lambda key: [key, gen_params.get(key, None)], generation_parameters)))

    return list(map(lambda x: f"{x[0]}: {x[1]}", gen_params_tags))