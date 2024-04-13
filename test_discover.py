import pytest

@pytest.mark.filterwarnings
def test_discover_screen(appium_driver):
    discover_title = appium_driver.find_element(by='id', value='com.zhiliaoapp.musically.go:id/a57')
    assert discover_title.is_displayed(), "Discover screen title is not displayed"

    discover_title.click()
    # Find all elements with the specified ID
