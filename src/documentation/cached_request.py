import os
import hashlib
import requests

import tempfile

cache_dir = os.path.join(tempfile.gettempdir(), "openmaya_cache")


def md5_hash(text: str) -> str:
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def request(url: str, use_cache: bool) -> str:
    cache_file = os.path.join(cache_dir, f"{md5_hash(url)}.html")

    if use_cache and os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            content = f.read()
        response = requests.Response()
        response.status_code = 200
        response._content = content
        response.url = url
        return response.text

    response = requests.get(url)
    response.raise_for_status()

    if use_cache:
        os.makedirs(cache_dir, exist_ok=True)
        with open(cache_file, 'wb') as f:
            f.write(response.content)

    return response.text
