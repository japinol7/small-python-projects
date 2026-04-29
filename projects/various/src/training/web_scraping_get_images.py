APP_NAME = 'Web Scraping - Get Images'
APP_VERSION = '0_00_1'

import base64
from io import BytesIO
import os
import tempfile
import subprocess
import webbrowser

from bs4 import BeautifulSoup
from PIL import Image
import requests


def _is_running_inside_kitty():
    return os.environ.get("TERM") == "xterm-kitty" \
        or "KITTY_PID" in os.environ


def _open_image_in_browser(buffer):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(buffer.getvalue())
        tmp.flush()
        webbrowser.open(f"file://{tmp.name}")


def _buffer_to_base64(buffer):
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def _open_gallery_in_browser(buffers):
    images_html = ""

    for buffer in buffers:
        img_base64 = _buffer_to_base64(buffer)
        images_html += f"""
            <div class="card">
                <img src="data:image/png;base64,{img_base64}" />
            </div>
        """

    html_content = f"""
    <html>
    <head>
        <title>{APP_NAME}  v. {APP_VERSION}</title>
        <style>
            body {{
                background: #111;
                color: white;
                font-family: Arial;
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                padding: 20px;
            }}
            .card img {{
                height: 300px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(255,255,255,0.3);
            }}
        </style>
    </head>
    <body>
        {images_html}
    </body>
    </html>
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w") as tmp:
        tmp.write(html_content)
        tmp.flush()
        webbrowser.open(f"file://{tmp.name}")


def _render_image_on_a_kitty_terminal(buffer):
    # Pipe to kitty icat
    proc = subprocess.Popen(
        ['kitty', '+kitten', 'icat', '--align', 'left'],
        stdin=subprocess.PIPE)
    proc.communicate(buffer.read())


def _display_images(buffers):
    if _is_running_inside_kitty():
        for buffer in buffers:
            _render_image_on_a_kitty_terminal(buffer)
        return
    _open_gallery_in_browser(buffers)


def _open_image_in_memory(url_im):
    response = requests.get(url_im)
    img = Image.open(BytesIO(response.content))
    img.thumbnail((600, 300))

    # Convert to PNG in memory
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer


def _get_all_images():
    res = requests.get("https://www.themoviedb.org/movie")
    soup = BeautifulSoup(res.text, 'html.parser')

    im_buffers = []
    for im in soup.find_all('img', attrs={'class': 'poster'}, limit=3):
        url_im = im['src']
        print(url_im)
        try:
            im_buffer = _open_image_in_memory(url_im)
            im_buffers.append(im_buffer)
        except Exception as e:
            print(e)

    _display_images(im_buffers)


def main():
    print(f"-- Start program {APP_NAME} {APP_VERSION} --")
    _get_all_images()
    print(f"-- End program {APP_NAME} {APP_VERSION} --")


if __name__ == '__main__':
    main()
