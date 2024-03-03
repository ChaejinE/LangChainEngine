import requests
import os
import logging

logging.basicConfig(level=logging.INFO)


def download_file_from_url(url: str, save_path: str) -> None:
    response = requests.get(url, save_path)
    try:
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            if os.path.exists(save_path):
                logging.info(f"Download Success on {save_path}")
            else:
                raise RuntimeError
        else:
            raise RuntimeError
    except Exception as e:
        logging.warning(
            f"Download Fail from {url}\nResponse Status : {response.status_code}"
        )
        logging.warning(e)
