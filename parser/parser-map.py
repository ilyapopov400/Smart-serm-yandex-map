import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from icecream import ic
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.common.exceptions import NoAlertPresentException
from tqdm import tqdm
from itertools import product
from selenium.common.exceptions import NoSuchElementException


class ParseYandexMap:
    url = 'https://yandex.ru/maps/'
    '''
    парсинг одной страницы yandex map
    search_query: поисковый запрос
    :return
    '''

    def __init__(self, search_query: str):
        self.search_query = search_query
        self.options_chrome = webdriver.ChromeOptions()
        self.options_chrome.add_argument(
            'user-data-dir=/Users/ilapopov/Library/Application Support/Google/Chrome/Default')
        # self.options_chrome.add_argument('--headless')

    def _parser(self):
        with webdriver.Chrome(options=self.options_chrome) as browser:
            browser.get(self.url)

            time.sleep(100)

    def __call__(self, *args, **kwargs):
        self._parser()


if __name__ == "__main__":
    ParseYandexMap(search_query="М.видео")()
