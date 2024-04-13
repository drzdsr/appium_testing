import pytest

@pytest.mark.filterwarnings
def test_discover_screen(appium_driver):

    discover_title = appium_driver.find_element(by='id', value='com.zhiliaoapp.musically.go:id/a57')
    assert discover_title.is_displayed(), "Discover screen title is not displayed"

    discover_title.click()
    # Find all elements with the specified ID
    element = appium_driver.find_element_by_xpath("//xpath/to/your/element")

    # Constructing the selector
    discover_search = appium_driver.AndroidUIAutomator('new UiSelector().text("Search").instance(0)')


    assert discover_search.is_displayed(), "Discover search bar is not displayed"

    discover_search.send_keys("hello")


#Find element by ID:
    element = appium_driver.find_element(by='id', value='your_element_id')
#Find element by XPath:
    element = driver.find_element(MobileBy.XPATH, "//xpath/to/your/element")
#Find element by Accessibility ID:
    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "your_accessibility_id")
#Find element by Class Name:
    element = driver.find_element(MobileBy.CLASS_NAME, "your_element_class_name")
#Find element by Name:
    element = driver.find_element(MobileBy.NAME, "your_element_name")
#Find element by Tag Name:
    element = driver.find_element(MobileBy.TAG_NAME, "your_element_tag_name")
#Find element by CSS Selector:
    element = driver.find_element(MobileBy.CSS_SELECTOR, "your_css_selector")
#Find element by Android UI Automator:
    element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'your_uiautomator_expression')