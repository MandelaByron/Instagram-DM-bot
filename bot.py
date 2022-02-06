from selenium import webdriver
import time,random

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import gspread


options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
# options.add_experimental_option("prefs",prefs)
#user_agents="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
#options.add_argument(f"user-agent={user_agents}")
options.set_capability("browserVersion", "96.0")
options.set_capability("platformName","Linux")
options.set_capability('browserName','chrome')
# options.set_capabilities(
#     {"browserName":"chrome",
#      "browserVersion":"95",
#      "goog:chromeOptions":{"extensions":[],"args":[]},
#      "platformName":"linux"}
# )
#15259ba8-7f58-4da5-9b36-c8a94d52c7dd
#driver=webdriver.Chrome("chromedriver.exe",options=options)
driver = webdriver.Remote(
    command_executor='http://34.125.40.19:4444/wd/hub',
    options=options
)

password='yourpassword'

email='enteryouremail'

message='Hey, this is DM bot, if interested in one, reply with YES'

delay_between_messages=2000

target_users=["webscraper2","_mandela_byron","allanday104"]

def auth(username,password):
    try:
        driver.get("https://instagram.com")
        time.sleep(random.randrange(2,6))
        
        input_username=driver.find_element_by_name('username')
        input_password=driver.find_element_by_name("password")
        
        input_username.send_keys(username)
        time.sleep(random.randrange(2,4))
        input_password.send_keys(password)
        time.sleep(random.randrange(2,4))
        input_password.send_keys(Keys.ENTER)
    except Exception as e:
        print(e)
        driver.quit()
        
def send_message(target_users,message):
    try:
        print('in loop')
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        print('clicked1')
        time.sleep(random.randrange(2,3))
        try:
            driver.find_element_by_xpath('//div[@class="mt3GC"]/button[@class="aOOlW   HoLwm "]').click()
        except:
            pass
        driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button").click()
        
        print('clicked2')
        
        
        for user in target_users:
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input").send_keys(user)
            time.sleep(random.randrange(2,5))
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]").find_element_by_tag_name('button').click()
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/div/button").click()
            time.sleep(5)
            
            
            text_area=driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_area.send_keys(message)
            time.sleep(random.randrange(3,5))
            text_area.send_keys(Keys.ENTER)
            print(f'Message Successfully sent to: {user}')
            driver.find_element_by_xpath('//div[@class="_2NzhO EQ1Mr"]/button[@class="wpO6b ZQScA "]').click()
        
    
    except Exception as err:
        print(err)
        driver.quit()
        
auth(email,password)
time.sleep(random.randrange(2,4))
send_message(target_users=target_users,message=message)
#driver.quit()

