from requests import get, post, exceptions

TIMEOUT = (3, 10)

class EagleAPI:
    def __init__(self, server_url: str = 'http://localhost', port: int = 41595):
        self.server_url = server_url
        self.port = port

    def base_url(self):
        return f"{self.server_url}:{self.port}"

    def url(self, path: str):
        return f"{self.base_url()}{path}"

    def request(self, path, method: str = "GET", json: dict = {}):
        try:
            if method == "GET":
                response = get(
                    url=self.url(path),
                    timeout=TIMEOUT
                )
            elif method == "POST":
                data = { key:value for key,value in json.items() if value is not None }

                response = post(
                    url=self.url(path),
                    json=data,
                    timeout=TIMEOUT
                )
            else:
                raise ValueError(f"Invalid method: {method}")
        except exceptions.RequestException as e:
            print(e)
            return None

        return response.json().get('data')

    # APPLICATION
    ## /api/application/info
    def info(self):
        return self.request("/api/application/info", "GET")

    # FOLDER
    ## /api/folder/create
    def create_folder(self, name: str, parent_id: int | None = None):
        return self.request(
            "/api/folder/create",
            "POST",
            json={
                "folderName": name,
                "parent": parent_id
            }
        )

    ## /api/folder/delete

    ## /api/folder/update

    ## /api/folder/list
    def list_folders(self):
        return self.request("/api/folder/list", "GET")

    ## /api/folder/listRecent
    def list_recent_folders(self):
        return self.request("/api/folder/listRecent", "GET")

    # ITEM
    ## /api/item/addFromURL
    def add_from_url(self, url: str, name: str, website: str | None = None, tags: list[str] | None = None, annotation: str | None = None, modificationTime: int | None = None, folderId: str | None = None, headers: str | None = None):
        return self.request(
            "/api/item/addFromURL",
            "POST",
            json={
                "url": url,
                "name": name,
                "website": website,
                "tags": tags,
                "annotation": annotation,
                "modificationTime": modificationTime,
                "folderId": folderId,
                "headers": headers
            }
        )

    ## /api/item/addFromURLs

    ## /api/item/addFromPath
    def add_from_path(self, path: str, name: str, website: str | None = None, tags: list[str] | None = None, annotation: str | None = None, folderId: str | None = None):
        return self.request(
            "/api/item/addFromPath",
            "POST",
            json={
                "path": path,
                "name": name,
                "website": website,
                "tags": tags,
                "annotation": annotation,
                "folderId": folderId
            }
        )

    ## /api/item/addFromPaths

    ## /api/item/addBookmark

    ## /api/item/info

    ## /api/item/thumbnail

    ## /api/item/list

    ## /api/item/moveToTrash

    ## /api/item/refreshPalette

    ## /api/item/refreshThumbnail

    ## /api/item/update

    # LIBRARY
    ## /api/library/info

    ## /api/library/history

    ## /api/library/switch
