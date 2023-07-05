# 각 업소에 대한 이미지 데이터 수집용
import sqlite3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from urllib import request
import time
import pandas as pd
pd.set_option("display.max_columns", None)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.naver.com/')

class Crawling:
    def __init__(self):
        self.dnum = 0
        tourist_attractions_data = pd.read_csv("./data/tourist_attractions_data.csv", encoding='cp949')
        tourist_attractions_name_data = list(tourist_attractions_data["여행지"].values)
        address_list = list()
        image_directory = 'C:/Users/KDT02/Desktop/new_team_project_1/image/'
        WEB_DRIVER_PATH = "C:/Users/KDT02/Desktop/chromedriver_win32/chromedriver.exe"
        s = Service(WEB_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.com/search?q=test&hl=ko&tbm=isch&source=hp&biw=1920&bih=969&ei=MB6lZJSJBq-m2roPmcSU-AE&iflsig=AD69kcEAAAAAZKUsQL8gqju5BcU9E9s6OiI7KGjQSbLe&ved=0ahUKEwiU4YX_h_f_AhUvk1YBHRkiBR8Q4dUDCAc&uact=5&oq=test&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgAEAM6CAgAELEDEIMBOgsIABCABBCxAxCDAVAAWI0CYLQFaABwAHgAgAGmAYgB7gSSAQMwLjSYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img")
        # XPATH와 FULLXPATH와는 다르구나. FULLXPATH로 하니까 되네...
        for idx, name in enumerate(tourist_attractions_name_data):
            try:
                input_box = WebDriverWait(driver, timeout=60).until(
                    lambda d: d.find_element(By.XPATH, '//*[@id="REsRA"]'))
                input_box.clear()
                input_box.send_keys(f"{name}")
                input_box.send_keys(Keys.RETURN)

                first_image = WebDriverWait(driver, timeout=60).until(
                    lambda d: d.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img'))

                first_image.click()
                big_image = WebDriverWait(driver, timeout=60).until(
                    lambda d: d.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]'))

                big_image_url = big_image.get_attribute('src')
                request.urlretrieve(big_image_url, image_directory + f"{name}.png")
                address_list.append(image_directory + f"{name}.png")
                print(address_list[-1])
            except Exception as e:
                address_list.append("-")
                print(idx, name, e)

            if idx == len(tourist_attractions_name_data):
                address_list_df = pd.DataFrame(address_list, columns=["이미지"])
                address_list_df.to_csv("./data/image_address.csv", index=False)
                tourist_attractions_data = pd.concat([tourist_attractions_data, address_list_df], axis=1)
                tourist_attractions_data.to_csv("./data/tourist_attractions_data_1.csv", index=False)



        # WEB_DRIVER_PATH = "C:/Users/KDT02/Desktop/chromedriver_win32/chromedriver.exe"
        # s = Service(WEB_DRIVER_PATH)
        # driver = webdriver.Chrome(service=s)
        # driver.get("https://map.naver.com/v5/?c=15,0,0,2,dh")
        # time.sleep(3)
        # # XPATH와 FULLXPATH와는 다르구나. FULLXPATH로 하니까 되네...
        # input_box = driver.find_element(By.XPATH,'/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div[1]/div/input')
        # input_box.send_keys("해운대")
        # input_box.send_keys(Keys.RETURN)
        # time.sleep(1)
        # driver.refresh()
        # inner_frame = driver.find_element(By.XPATH, '/html')
        # driver.switch_to.frame(inner_frame)
        #
        # sample = driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/div[2]/a[1]')
        # sample.execute_scripts("arguments[0].click();", sample)








if __name__ == '__main__':
    crawling_object = Crawling()
