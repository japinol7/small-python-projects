APP_NAME = 'Open image in web browser'
APP_VERSION = '0_01_0'

import os
import tempfile
import webbrowser
from io import BytesIO

from PIL import Image

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

FILE_INPUT_PATH = os.path.join(__location__, '..', "res", 'im')


def open_image_in_browser(buffer):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(buffer.getvalue())
        tmp.flush()
        webbrowser.open(f"file://{tmp.name}")


def _convert_image_to_png_in_memory(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


def open_image_in_memory(file_name):
    file_path_name = os.path.join(FILE_INPUT_PATH, file_name)
    img = Image.open(file_path_name)

    img.thumbnail((600, 300))
    return _convert_image_to_png_in_memory(img)


def main():
    print(f"-- Start program {APP_NAME} {APP_VERSION} --")

    img = open_image_in_memory("movie_alien_ridley scott.png")
    open_image_in_browser(img)

    print(f"-- End program {APP_NAME} {APP_VERSION} --")


if __name__ == '__main__':
    main()
