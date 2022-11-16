# WinInstaller 1.0
author: Patric

version: 0.1

```
.
│   README.txt 
│   __init__.py //main file, can be imported
│
├───Authentication
│       __init__.py //TODO: Authentication
│
├───Console
│       __init__.py //interface with winget.exe
│
└───Test
        framelesswindow.py //custom window
```

Release notes:
- main GUI is created (win11 only)
- all menu bars are handled \(TODO, check ```./\_\_init\_\_.py``` for more information\)

What is missing:
- search engine
- search bar
- different pages (home almost done)
- fallbacks
- automatic execution
- winget interface
- API calls