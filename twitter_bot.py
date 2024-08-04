from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pt

promised_down = 150
promised_up = 10


t_user = ''
t_pwd = ''
wrong_user = 'wrong_user@cmrit.ac.in'
wrong_pwd = 'wrongpassword'


class InternetSpeedTwitterBot:
    def _init_(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get('https://www.speedtest.net/')
        time.sleep(3)
        try:
            cross = self.driver.find_element(By.XPATH,
                                             '/html/body/div[5]/div[2]/div/div/div[2]/div[1]/div/button')
            cross.click()
        except NoSuchElementException:
            print("Element Not Found")
            exit(0)
        time.sleep(3)
        try:
            button = self.driver.find_element(
                By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            button.click()

            time.sleep(50)
            self.up = self.driver.find_element(
                By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            self.down = self.driver.find_element(
                By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

            print(self.up)
            print(self.down)
        except NoSuchElementException as e:
            print(e)

    def tweet_at_provider(self, username, password):
        self.driver.maximize_window()
        self.driver.get(
            'https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D')
        time.sleep(5)
        try:
            user = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'text'))
            )
            user.send_keys(username)
            user.send_keys(Keys.ENTER)

            pwd = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            pwd.send_keys(password)
            pwd.send_keys(Keys.ENTER)

            time.sleep(7)

            if "login error" in self.driver.page_source.lower():
                print("Login failed. Check your username and password.")
                return

            tweet_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'))
            )
            tweet_button.click()
            time.sleep(5)

            pt.write(
                "Hey Twitter. WHY MY INTERNET speed is so slow when I am paying good money.")
            time.sleep(5)

            pt.click(x=1352, y=627)
            # print(pt.position())
            time.sleep(5)
        except (NoSuchElementException, TimeoutException) as e:
            print(e)
        # finally:
        #     self.driver.quit()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()

print("Testing with incorrect credentials:")
bot.tweet_at_provider(wrong_user, wrong_pwd)
print("The credentials are incorrect.")

print("Testing with correct credentials:")
bot.tweet_at_provider(t_user, t_pwd)
