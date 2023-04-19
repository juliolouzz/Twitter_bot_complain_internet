from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10
INTERNET_PROVIDER = ""  # "Your @Internet Provider"
TWITTER_LOGIN = ""  # "Your email, login or number"
TWITTER_PASSWORD = ""  # "Your password"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(1)
        accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies.click()
        sleep(1)
        btn_go = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        btn_go.click()
        sleep(60)
        ads_close = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[3]/div/div[8]/div/div/div[2]/a')
        ads_close.click()
        sleep(1)
        download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                      '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                      '1]/div/div[2]/span')
        upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = download.text
        self.up = upload.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        sleep(1)
        cookies = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
        cookies.click()
        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div['
                                                   '2]/div/div/div[1]/a')
        login.click()
        sleep(2)
        twitter_login_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                                 '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
                                                                 '5]/label/div/div[2]/div/input')
        twitter_login_field.send_keys(TWITTER_LOGIN)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_btn.click()
        sleep(2)
        twitter_password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div['
                                                                    '2]/div/div/div/div/div/div[2]/div['
                                                                    '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                                    '3]/div/label')
        twitter_password_field.send_keys(TWITTER_PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_btn.click()
        sleep(3)
        second_cookies = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
        second_cookies.click()
        sleep(3)
        twitter_write = self.driver.find_element(By.CSS_SELECTOR,
                                                 "div.notranslate.public-DraftEditor-content[aria-label='Tweet text']")
        twitter_write.send_keys(f"Hey {INTERNET_PROVIDER}, why is my internet speed {self.down}down/{self.up}up when "
                                f"I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(2)
        send_message = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                          '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                          '3]/div/div/div[2]/div[3]')
        send_message.click()
        sleep(3)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
