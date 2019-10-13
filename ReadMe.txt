Had written the automation test in Python programming language.

Library Required:

1.Selenium

To install run the below command:
pip install selenium==2.53.6


Setting environment variable:

Need to set PATH for chrome driver. [It will change the dependending on the OS you were working ]

Below steps is written for mac o/s.
Steps:
1. vi ~/.bash_profile
2. Update path variable to locate chrome webdriver.

export PATH=/usr/local/bin/:$PATH:<specify the local path where chrome driver is present>

Note: To get chrome driver, refer below site. Download the version based on the chrome version running local on your system.
https://chromedriver.chromium.org/downloads

3. source ~/.bash_profile


To run the scripts, run below command

python Test1.py
python Test2.py


Note: Documentations had been provided in code to explain which part is doing which steps.



