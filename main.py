from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import random

CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe'
SIMILAR_ACCOUNT = 'addisalem_getaneh'
USERNAME = 'account'
PASSWORD ='password' 

class InstaFollower:
    def __init__(self, path: str):
        service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=service)
    def login(self):
        self.driver.get(url=" https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usr_name = self.driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        usr_name.send_keys(USERNAME)
        password = self.driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
    def find_followers(self):
        time.sleep(60)
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(10)


    def follow(self):
        for i in range(1, 50):
            time.sleep(random.randint(1,5))
            account =  self.driver.find_element(by='xpath', value=f"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/button")
            if account.text == "follow":
                account.click()
            else:
                continue
            if i == 15:
                modal = self.driver.find_element(by='xpath', value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

follower_bot = InstaFollower(path=CHROME_DRIVER_PATH)
follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()
time.sleep(200)


