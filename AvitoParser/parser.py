from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from AvitoParser.config import URL, Token_words
import time


class AvitoParser:
    def __init__(self, url, driver_version="122.0.6261.95"):
        # URL:
        self.url = url
        # web-driver options:
        self.options = webdriver.ChromeOptions()
        # fake user-agent:
        self.User_Agent = UserAgent()
        self.user_agent = UserAgent.random
        # add options:
        self.options.add_argument(f"user-agent={self.user_agent}")
        # Chrome web-driver:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version=driver_version).install()),
                                       options=self.options)
        # init pages of sites:
        self.site_pages = []
        # init ads array:
        self.ads = []

    # get requests on avito page:
    def get_requests(self):
        self.driver.get(self.url)
        time.sleep(10)

    # this method click on window of ads:
    def click_ads_window(self, iterator):
        items = self.driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")
        items[iterator].click()
        time.sleep(10)

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(10)

    # this method find on page info of sector:
    def get_sector_info(self):
        sector_info = self.driver.find_elements(By.XPATH, "//h1[@data-marker='item-view/title-info']")
        time.sleep(10)
        for word in range(len(Token_words)):
            if not(Token_words[word] in sector_info[0].text):
                self.ads.append(sector_info[0].text)
            else:
                self.ads.append(None)

    # this method return sale of sector:
    def get_sale(self):
        sector_sale = self.driver.find_elements(By.CLASS_NAME, "style-item-price-sub-price-_5RUD")
        self.ads.append(sector_sale[0].text[:-9])
        time.sleep(10)

    def get_area(self):
        area = self.driver.find_elements(By.CLASS_NAME, "params-paramsList__item-_2Y2O")
        self.ads.append(area[0].text[9:12])
        time.sleep(10)

    # this method return address of sector:
    def get_location(self):
        location = self.driver.find_elements(By.CLASS_NAME, "style-item-address__string-wt61A")
        self.ads.append(location[0].text)
        time.sleep(10)

    # this method return current URL of page ads:
    def get_url(self):
        self.ads.append(self.driver.current_url)

    # this method close sector window ads:
    def close_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(15)

    # parse avito page:
    def get_parse(self):
        try:
            for i in range(7):
                self.get_requests()
                self.click_ads_window(i)
                self.get_sector_info()
                if not(self.ads[0] == None):
                    self.get_sale()
                    self.get_area()
                    self.get_location()
                    self.get_url()
                    self.close_window()
                    # append ads page in table:
                    self.site_pages.append(self.ads)
                else:
                    self.ads.pop(0)
                    # close window:
                    self.close_window()
        except Exception as _ex:
            print(_ex)
        finally:
            self.driver.close()
            self.driver.quit()

        return self.site_pages


avito = AvitoParser(URL)
ads = avito.get_parse()
print(ads)