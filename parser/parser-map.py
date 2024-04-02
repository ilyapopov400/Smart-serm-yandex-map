import time
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from icecream import ic
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.common.exceptions import NoAlertPresentException
from tqdm import tqdm
from itertools import product
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url_find = "https://yandex.ru/maps/38/volgograd/chain/video/6002372/?ll=44.518709%2C48.707615&sll=44.516979%2C48.707068&sspn=0.177155%2C0.188825&z=11.97"
url_find_1 = "https://yandex.ru/maps/org/m_video/1117900066/?ll=44.497380%2C48.749279&mode=search&sll=44.516979%2C48.707068&sspn=0.493011%2C0.188825&text=%D0%9C.%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE&z=12"


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
        element = element.find_element(By.CSS_SELECTOR, "input.input__control")
        element.send_keys(self.search_query)  # запись в строке поиска

        element = browser.find_element(By.CLASS_NAME, "body")
        element = element.find_element(By.CLASS_NAME, "app")
        element = element.find_element(By.CSS_SELECTOR, "div.header-view__main-layout")
        element = element.find_element(By.CSS_SELECTOR, "div.small-search-form-view__button")
        element = element.find_element(By.TAG_NAME, "button")
        element.click()

    @staticmethod
    def _drop_down_windows(browser):
        """
        список выпавших элементов по поисковому запросу
        :param browser:
        :return:
        """
        element = browser.find_element(By.CLASS_NAME, "body")
        element = element.find_element(By.CLASS_NAME, "app")
        element = element.find_element(By.CSS_SELECTOR, "div.scroll__container")
        elements = element.find_elements(By.CSS_SELECTOR, "li.search-snippet-view")
        return elements

    @staticmethod
    def _touch_element_and_get_address_phone(browser, element):
        phone = None
        element.click()
        locator_address = (By.CSS_SELECTOR, "div.business-contacts-view__address")
        target_address = WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator_address))
        address = target_address.text

        try:
            locator_phone = (By.CSS_SELECTOR, "div.card-phones-view__more")
            target_phone = WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator_phone))
            target_phone.click()

            locator_phone2 = (By.CSS_SELECTOR, "div.card-phones-view__phone-number")
            target_phone2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator_phone2))
            phone = target_phone2.text

        except selenium.common.exceptions.TimeoutException:
            pass

        time.sleep(3)
        return address, phone

    def _parser(self):
        with webdriver.Chrome(options=self.options_chrome) as browser:
            result = list()
            browser.maximize_window()  # на весь экран
            browser.get(self.url)
            self._put_find(browser=browser)
            time.sleep(10)
            elements = self._drop_down_windows(browser=browser)
            for element in elements:
                address, phone = self._touch_element_and_get_address_phone(browser=browser, element=element)
                time.sleep(3)
                result.append({
                    "address": address,
                    "phone": phone
                })

            return result

    def __call__(self, *args, **kwargs):
        return self._parser()


def mane():
    result = ParseYandexMap(search_query="М.видео")()
    ic(result)


if __name__ == "__main__":
    mane()
