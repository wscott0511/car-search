import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

executable_path = "/Users/ryanscott/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://www.barrett-jackson.com/")

sleep = time.sleep(2)

search = "ford ac cobra"

sleep
#search for ac cobra
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div/ul/li[9]/form/div/div/input").send_keys(search)
#submit the search
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div/ul/li[9]/form/div/div/button").click()
sleep

#click on first entry
driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div[2]/div/div/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a").click()