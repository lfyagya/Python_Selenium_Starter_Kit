# Selenium Python Starter Kit

This is a starter kit for setting up a Selenium project with Python using the Page Object Model (POM) structure.
Document Link: https://docs.google.com/document/d/1_sglLM5AnCgm41qooqz66uLTOe9_r4b8FD4jqgI29sc/edit?usp=sharing

## Project Structure

- **Pages/**: Contains all the page classes.
- **Tests/**: Contains all the test cases.
- **Utils/**: Contains utility classes and methods.
- **Config/**: Contains configuration files and settings.
- **conftest/**: Define fixtures and configuration for pytest. It includes the fixture, which is responsible for setting up and tearing down the web driver for your Selenium tests.

## Setup

1. Clone the repository:
```bash
git clone git@github.com:lfyagya/Python_Selenium_Starter_Kit.git
```
2. Install Pipenv if not already installed:
```bash
pip install pipenv
```
3. Install dependencies:
```bash
pipenv install
```
4. Activate the virtual environment:
```bash
pipenv shell
```
7. Run tests: `pytest {test folder name}/{test script file name}:` 
```bash
pytest Test/test_login.py
```
