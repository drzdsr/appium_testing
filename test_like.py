import pytest

@pytest.mark.filterwarnings
def test_discover_screen(appium_driver):
    like = appium_driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/rk')
    assert like.is_displayed(), "like button is not displayed"
    like.click()

    appium_driver.back()
