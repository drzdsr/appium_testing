Command to run Appium Server
    appium -p 4723

Commands to run in terminal to start AVD
    emulator -avd pixel

    
Code To get appPackage and appActivity
    Open APP in phone / emulator and hide
    Run adb shell
    Run Given Command
        dumpsys window windows | grep -E 'mTopActivityComponent'

#Find element by ID:
    element = appium_driver.find_element(by='id', value='your_element_id')
#Find element by XPath:
    element = appium_driver.find_element(MobileBy.XPATH, "//xpath/to/your/element")
#Find element by Accessibility ID:
    element = appium_driver.find_element(MobileBy.ACCESSIBILITY_ID, "your_accessibility_id")
#Find element by Class Name:
    element = appium_driver.find_element(MobileBy.CLASS_NAME, "your_element_class_name")
#Find element by Name:
    element = appium_driver.find_element(MobileBy.NAME, "your_element_name")
#Find element by Tag Name:
    element = appium_driver.find_element(MobileBy.TAG_NAME, "your_element_tag_name")
#Find element by CSS Selector:
    element = appium_driver.find_element(MobileBy.CSS_SELECTOR, "your_css_selector")
#Find element by Android UI Automator:
    element = appium_driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'your_uiautomator_expression')


#Find elements by ID (multiple elements):
    elements = appium_driver.find_elements(MobileBy.ID, "your_element_id")
#Find elements by XPath (multiple elements):
    elements = appium_driver.find_elements(MobileBy.XPATH, "//xpath/to/your/elements")
#Find elements by Accessibility ID (multiple elements):
    elements = appium_driver.find_elements(MobileBy.ACCESSIBILITY_ID, "your_accessibility_id")
#Find elements by Class Name (multiple elements):
    elements = appium_driver.find_elements(MobileBy.CLASS_NAME, "your_element_class_name")
#Find elements by Name (multiple elements):
    elements = appium_driver.find_elements(MobileBy.NAME, "your_element_name")
#Find elements by Tag Name (multiple elements):
    elements = appium_driver.find_elements(MobileBy.TAG_NAME, "your_element_tag_name")
#Find elements by CSS Selector (multiple elements):
    elements = appium_driver.find_elements(MobileBy.CSS_SELECTOR, "your_css_selector")
#Find elements by Android UI Automator (multiple elements):
    elements = appium_driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, 'your_uiautomator_expression')


for element in elements:
    print(element.text)

element.click()
element.send_keys("hello")

