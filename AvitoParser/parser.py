# for work with chrome:
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
# page url:
from AvitoParser.config import AVITO_URL
# supporting method/function:
import time
from AvitoParser.Project_Lib import sector_filter
from AvitoParser.Project_Lib import avito_datetime
# fake proxy:
from AvitoParser.Proxy.proxy_auth_data import proxy_options


class AvitoParser:
    def __init__(self, url, ads_number, driver_version="122.0.6261.95"):
        # URL:
        self.url = url
        # web-driver options:
        self.options = webdriver.ChromeOptions()
        # fake user-agent:
        self.User_Agent = UserAgent()
        self.user_agent = UserAgent.random
        # add options user-agent:
        self.options.add_argument(f"user-agent={self.user_agent}")
        # Chrome web-driver:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version=driver_version).install()),
                                       seleniumwire_options=proxy_options,
                                       options=self.options)
        # init pages of sites:
        self.site_pages = []
        # number of ads:
        self.ads_number = ads_number

    # get requests on avito page:
    def get_requests(self, url):
        self.driver.get(url)
        time.sleep(10)

    # this method click on window of ads:
    def click_ads_window(self, iterator):
        items = self.driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")
        items[iterator].click()
        time.sleep(10)

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(10)

    # this method find on page info of sector:
    def get_sector_info(self, ads):
        sector_info = self.driver.find_elements(By.XPATH, "//h1[@data-marker='item-view/title-info']")
        self.driver.implicitly_wait(10)
        if sector_filter.check_sector(sector_info[0].text):
            ads.append(sector_info[0].text)
        else:
            ads.append(None)

    # this method return sale of sector:
    def get_sale(self, ads):
        sector_sale = self.driver.find_elements(By.CLASS_NAME, "style-item-price-sub-price-_5RUD")
        ads.append(int(sector_sale[0].text[:-11].replace(' ', '')))
        self.driver.implicitly_wait(10)

    def get_area(self, ads):
        try:
            area = self.driver.find_elements(By.CLASS_NAME, "params-paramsList__item-_2Y2O")
            ads.append(float(area[0].text[9:12].replace(' ', '')))
            self.driver.implicitly_wait(10)
        except Exception as _ex:
            print(_ex)
            ads.append(None)

    # this method return address of sector:
    def get_location(self, ads):
        location = self.driver.find_elements(By.CLASS_NAME, "style-item-address__string-wt61A")
        ads.append(location[0].text)
        self.driver.implicitly_wait(10)

    # this method return datetime of sector ads:
    def get_datetime(self, ads):
        ads_datetime = self.driver.find_elements(By.XPATH, "//span[@data-marker='item-view/item-date']")
        ads.append(avito_datetime.current_date(ads_datetime[0].text))
        self.driver.implicitly_wait(10)

    # this method return current URL of page ads:
    def get_url(self, ads):
        ads.append(self.driver.current_url)

    # this method return last number of page (int):
    def get_number_paginator(self):
        pages = self.driver.find_elements(By.XPATH, "//li[@class='styles-module-listItem-_La42 styles-module-listItem_last-GI_us styles-module-listItem_notFirst-LGEQU']")
        return int(pages[0].text)

    # this method close sector window ads:
    def close_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.implicitly_wait(15)

    # parse avito page:
    def get_parse(self):
        try:
            # first page:
            avito_url = self.url + '1'
            self.get_requests(avito_url)
            # number of last page:
            last_page_number = self.get_number_paginator()
            # pages loop:
            for page in range(1, 3):
                i = 0
                if page != 1:
                    avito_url = avito_url.replace(avito_url[-1], f"{page}")
                    self.get_requests(avito_url)
                else:
                    pass
                while i < self.ads_number:
                    # ads array:
                    ads = []
                    self.click_ads_window(i)
                    self.get_sector_info(ads=ads)
                    if ads[0] is not None:
                        self.get_sale(ads=ads)
                        self.get_area(ads=ads)
                        self.get_location(ads=ads)
                        self.get_datetime(ads=ads)
                        self.get_url(ads=ads)
                        # append ads page in table:
                        self.site_pages.append(ads)
                        # close window:
                        self.close_window()
                    else:
                        ads.pop(0)
                        # close window:
                        self.close_window()
                    i += 1
        except Exception as _ex:
            print(_ex)
        finally:
            self.driver.close()
            self.driver.quit()

        return self.site_pages

