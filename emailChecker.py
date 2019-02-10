#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     11/01/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import needed object
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup



email = input("Entrez l'adresse mail")
#put the url of the site into the object url of type str
url = "http://mailtester.com/testmail.php"
#initialise the object options with the options of chrome webdriver, return the object options of type selenium.webdriver.chrome.options.Options
options = Options()
#define the option of chrome webdriver,Returns whether or not the headless argument is set
options.headless = True
#create a webdriver object, return the object driver of type selenium.webdriver.chrome.webdriver.WebDriver
driver = webdriver.Chrome(options=options)
#get the url, return an object of type NoneType
driver.get(url)

#select the bar search
barSearch = driver.find_element_by_name("email")
#write the email address in the bar search
barSearch.send_keys(email)

#select the submit button
button = driver.find_element_by_class_name("Button")
#click the button
button.click()

#create a beautifulsoup object, return an object of type bs4.BeautifulSoup
soup = BeautifulSoup(driver.page_source,features="html.parser")

result = soup.select("td")
success = result[-1].text
if success == "E-mail address is valid":
    return ("1")
else :
    return ("False")

