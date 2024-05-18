# Selenium-Python-Project

This repository contains the base setup of an UI testing project,
using Python, Selenium Webdriver and Page Object Model pattern.

# Requirements

* Python 3.12.X
* pip and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory "/selenium-python-example/".
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -s -v -n=2 --html=Reports/report.html tests/test_vocabulary.py --browser chrome


# Results

To check the report, open the '/results/report.html' file once the execution has finished.


   