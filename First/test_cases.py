#import requests
#import selenium as selenium

#response = requests.get('https://makeup.com.ua/')
#if response.status_code == 200:
    #print('successfull')

from selenium import webdriver
from selenium.webdriver.common.by import By
#pip install selenium
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('ignore-certificate-errors')
#
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
#docker run -d -p 4444:4444 -p 5900:5900 -v /dev/shn selenium/standalone-chrome-debug


url_variable = 'Shampoo'
url=['https://makeup.com.ua/']
driver.get(url[0])
element_address = '//*[@id="search-input"]'
element=driver.find_element(By.XPATH, element_address)
element.send_keys(url_variable)


