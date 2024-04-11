import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': '11100253B3020296',
    'appPackage': 'com.zhiliaoapp.musically.go',
    'appActivity': 'com.ss.android.ugc.aweme.main.homepage.MainActivity',
    'noReset': True,
    'language': 'en',
    'locale': 'US'
}

appium_server_url = 'http://localhost:4723'
driver: WebDriver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))

time.sleep(1)
for i in range(5):
    driver.swipe(100, 300, 100, end_y= 50)
    time.sleep(1)

like = driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/rk')
like.click()

commentBtn = driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/ou')
commentBtn.click()

newComment = driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/a0k')
newComment.send_keys('Hi')

submitComment = driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/abo')
submitComment.click()

driver.back()

discoverBtn = driver.find_element(By.XPATH, '//*[@resource-id="com.zhiliaoapp.musically.go:id/a57"]/android.widget.ImageView')
discoverBtn.click()

#Error From Here Above code is Working
discoverSearchBtn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='SearchSearch')
discoverSearchBtn.click()

Search = driver.find_element(By.XPATH, '//*[@resource-id="com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Search"]]')
Search.click()


driver.quit()

