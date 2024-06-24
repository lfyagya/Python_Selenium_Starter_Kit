# Selenium Python Starter Kit

This is a starter kit for setting up a Selenium project with Python using the Page Object Model (POM) structure.

## Project Structure

- **Pages/**: Contains all the page classes.
- **Tests/**: Contains all the test cases.
- **Utils/**: Contains utility classes and methods.
- **Config/**: Contains configuration files and settings.
- **conftest/**: Define fixtures and configuration for pytest. It includes the fixture, which is responsible for setting up and tearing down the web driver for your Selenium tests.

## Setup

1. Clone the repository: ``git clone git@github.com:lfyagya/Python_Selenium_Starter_Kit.git``.
2. Install Pipenv if not already installed: `pip install pipenv`
3. Install dependencies: `pipenv install`
4. Activate the virtual environment: `pipenv shell`
5. Run tests: `pytest {test folder name}/{test script file name}: pytest Test/test_login.py`
