# 각 업소에 대한 이미지 데이터 수집용
import sqlite3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from urllib import request
import time


class Crawling:
    def __init__(self):
        image_directory = 'C:/Users/KDT02/Desktop/new_team_project/song/image/'
        WEB_DRIVER_PATH = "C:/Users/KDT02/Desktop/chromedriver_win32/chromedriver.exe"
        s = Service(WEB_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.kr/")
        # XPATH와 FULLXPATH와는 다르구나. FULLXPATH로 하니까 되네...
        input_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        input_box.send_keys("해운대")
        input_box.send_keys(Keys.RETURN)
        image_button = driver.find_element(By.XPATH, '//*[@id="cnt"]/div[5]/div/div/div[1]/div[1]/div/a[2]')
        image_button.click()
        first_image = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
        first_image.click()
        big_image = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]')
        big_image_url = big_image.get_attribute('src')
        request.urlretrieve(big_image_url, image_directory + "해운대.png")


        while True:
            pass

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
