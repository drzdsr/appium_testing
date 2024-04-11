@echo off

REM Start Android emulator
start emulator -avd pixel
IF ERRORLEVEL 1 (
    echo Error: Failed to start Android emulator.
    EXIT /B 1
)

REM Start Appium server
start appium -p 4723
IF ERRORLEVEL 1 (
    echo Error: Failed to start Appium server.
    EXIT /B 1
)

REM Start Appium Inspector
start "" "C:\Users\MrDD\AppData\Local\Programs\Appium Inspector\Appium Inspector.exe"
IF ERRORLEVEL 1 (
    echo Error: Failed to start Appium Inspector.
    EXIT /B 1
)

REM Start Code Editor (replace "code" with the actual editor executable if needed)
start code
IF ERRORLEVEL 1 (
    echo Error: Failed to start code editor.
    EXIT /B 1
)

echo All processes started successfully.
