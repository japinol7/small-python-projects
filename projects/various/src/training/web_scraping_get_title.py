APP_NAME = 'Web Scraping - Get Title'
APP_VERSION = '0_00_1'

import requests
from bs4 import BeautifulSoup


def _get_page_title():
    res = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
    soup = BeautifulSoup(res.text, 'html.parser')
    print(f"Website title: {soup.title.string}")


def main():
    print(f"-- Start program {APP_NAME} {APP_VERSION} --")
    _get_page_title()
    print(f"-- End program {APP_NAME} {APP_VERSION} --")


if __name__ == '__main__':
    main()
