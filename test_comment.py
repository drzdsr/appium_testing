import pytest

@pytest.mark.filterwarnings
def test_discover_screen(appium_driver):
    comment_button = appium_driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/ou')
    assert comment_button.is_displayed(), "Comment Button is not displayed"
    comment_button.click()

    new_comment = appium_driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/a0k')
    assert new_comment.is_displayed(), "Comment prompt is not displayed"
    new_comment.send_keys('Hi')

    submit_comment = appium_driver.find_element(by=AppiumBy.ID, value='com.zhiliaoapp.musically.go:id/abo')
    assert submit_comment.is_displayed(), "Comment submit button is not displayed"
    submit_comment.click()
    appium_driver.back()