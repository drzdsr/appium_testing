Command to run Appium Server
    appium -p 4723

Commands to run in terminal to start AVD
    emulator -avd pixel

    
Code To get appPackage and appActivity
    Open APP in phone / emulator and hide
    Run adb shell
    Run Given Command
        dumpsys window windows | grep -E 'mTopActivityComponent'



