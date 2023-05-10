from selenium import webdriver
from selenium.webdriver.common.by import By
EXE_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path = EXE_PATH)
driver.get('https://dzen.ru/')
element = driver.find_element(By.CLASS_NAME, 'geoblock-weather__currentWeather-1P')
element.click()