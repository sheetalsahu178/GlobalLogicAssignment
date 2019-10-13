from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.common.keys import Keys
import csv


# Initialize ChromeDriver and Luanching the discovery website -Step 1

driver=webdriver.Chrome()
website_URL = "https://go.discovery.com/"
driver.get(website_URL)
wait = WebDriverWait(driver, 50)
driver.maximize_window()

# Scroll Down to Popular Shows option - Step 2

find_elem = None
scroll_from = 0
scroll_limit = 3000
while not find_elem:
    sleep(2)
    driver.execute_script("window.scrollTo(%d, %d);" %(scroll_from, scroll_from+scroll_limit))
    scroll_from += scroll_limit
    try:
        find_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-root\"]/div/div[1]/section[9]/div/div[1]/h2")))
    except TimeoutException:
        pass


# Going to the last video by pressing > - Step 3

get_ele= driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div[1]/section[9]/div/div[1]/div[2]/ul")
html_list = driver.find_element_by_class_name("popularShowsCarousel__pager")
items = html_list.find_elements_by_tag_name("li")
for item in items:
    item.click()


# Click on "Explore the show" and Clion on "Show more" option two times
# Step  - 4, 5 and 6

sleep(10)
driver.get("https://go.discovery.com/tv-shows/deadliest-catch/")
sleep(10)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
sleep(10)
driver.find_element_by_class_name("episodeList__showMore").click()
sleep(10)
driver.find_element_by_class_name("episodeList__showMore").click()


# Create a csv file and writing show titles and duration on it. Step - 7


html_list = driver.find_element_by_class_name("episodeList__list")
items = html_list.find_elements_by_tag_name("li")
for item in items:
    with open('data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([item.text])