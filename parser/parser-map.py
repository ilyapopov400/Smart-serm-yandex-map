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

    def _put_find(self, browser):
        """
        В поле поиска вставляем запрос и нажимаем найти
        :return:
        """
        element = browser.find_element(By.CLASS_NAME, "body")
        element = element.find_element(By.CLASS_NAME, "app")
        element = element.find_element(By.CSS_SELECTOR, "div.header-view__main-layout")
        element = element.find_element(By.TAG_NAME, "input")
        element.send_keys(self.search_query)  # запись в строке поиска

        element = browser.find_element(By.CLASS_NAME, "body")
        element = element.find_element(By.CLASS_NAME, "app")
        element = element.find_element(By.CSS_SELECTOR, "div.header-view__main-layout")
        element = element.find_element(By.CSS_SELECTOR, "div.small-search-form-view__button")
        element = element.find_element(By.TAG_NAME, "button")
        element.click()

    def _parser(self):
        with webdriver.Chrome(options=self.options_chrome) as browser:
            browser.get(self.url)
            self._put_find(browser=browser)

            time.sleep(10)

    def __call__(self, *args, **kwargs):
        self._parser()


if __name__ == "__main__":
    ParseYandexMap(search_query="М.видео")()
