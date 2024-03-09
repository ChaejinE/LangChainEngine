import requests
import os
import logging

logging.basicConfig(level=logging.INFO)


def download_file_from_url(url: str, save_path: str) -> None:
    response = None

    try:
        response = requests.get(url, save_path)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            if os.path.exists(save_path):
                logging.info(f"{__file__}\nDownload Success on {save_path}")
            else:
                raise RuntimeError
        else:
            raise RuntimeError
    except Exception as e:
        logging.warning(
            f"{__file__}\nDownload Fail from {url}\nResponse Status : {response.status_code}\n{e}"
        )
