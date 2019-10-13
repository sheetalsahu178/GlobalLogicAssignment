from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


xpathshowtab= "//*[@id=\"react-root\"]/div/div[1]/div[2]/header/div[2]/div/nav/ul/li[2]/span"
xpathshowallshows= "//div[@id='show-drop-desktop']/ul[1]/li[11]/div[@class='dscShowsDropContent__seeAllShowsContainer' and 1]/a[@class='dscShowsDropContent__seeAllShows' and 1]"


# Initialize ChromeDriver and Luanching the discovery website -Step 1

driver=webdriver.Chrome()
website_URL = "https://go.discovery.com/"
driver.get(website_URL)
wait = WebDriverWait(driver, 50)
driver.maximize_window()

# Select See All Shows available in Shows tab - Step - 2

driver.find_element_by_xpath(xpathshowtab).click()
res= driver.find_element_by_xpath(xpathshowallshows).get_attribute("href")
driver.get(res)


# Wait till the page loads and then select the shows which contain APOLLO

find_elem = None
scroll_from = 0
scroll_limit = 3000
while not find_elem:
    sleep(2)
    driver.execute_script("window.scrollTo(%d, %d);" %(scroll_from, scroll_from+scroll_limit))
    scroll_from += scroll_limit
    try:
        find_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-root\"]/div/div[1]/main/section/div/div[2]/div[30]/div/a/div/img")))
    except TimeoutException:
        pass

# Intailize the list for further verification

apollolist= []
favlist=[]

# Selecting the Shows which contain APOLLO - Step 3

html_list= driver.find_elements_by_tag_name("a")
for ele in html_list:
    res= ele.get_attribute("href")
    if str(res).find("apollo") != -1:
            apollolist.append(str(res))

# Launch the Apollo site and verifying whether it is in favourite list or not, by clicking the tooltip messgae
# Making it unfavourite if it is favourite and vise versa
#  Step - 4, 5 , 6 and 7


for item in apollolist:
    driver.get(item)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    sleep(5)
    titname=driver.find_element_by_xpath("//img[@class='showHero__showLogo']").get_attribute("alt")

    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div[1]/main/section[1]/div/div[1]/div[2]/div[1]/span/i")).perform()
    tool_tip_elm = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='react-tooltip-lite']")))

# Storing the fav in list
    if tool_tip_elm.text == "Add to My Favorites":
        driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div[1]/main/section[1]/div/div[1]/div[2]/div[1]/span/i").click()
        favlist.append(titname)
    else:
        print "Show is already added in the Fav list"



sleep(10)

# Once favorite or unfavorite is done, goto My Videos. Step -8

driver.find_element_by_xpath("//li[@class='dscHeaderMain__hideMobile']").click()
res=driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div[1]/div[2]/header/nav/div[2]/div/div/div[2]/div[2]/ul/li[4]/a").get_attribute("href")
# print res
driver.get(res)

sleep(10)

# Validate the favorite or unfavorite titles under FAVORITE SHOWS Step - 9

favshowlist=[]

html_list= driver.find_elements_by_tag_name("a")
for ele in html_list:
    res= ele.get_attribute("href")
    if str(res).find("apollo") != -1:
        favshowlist.append(str(res))

# verfiy the apollolist and favshowlist are same


if favshowlist == favshowlist:
    print ("The lists are identical, Favourite list contains the items got selected at step -3 ")
else:
    print ("The lists are not same")

