# conftest.py

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
@pytest.fixture(scope='session')
def appium_driver():
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
    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))

    yield driver

    driver.quit()
