# Automation Challenge Python-Selenium  
  
This is an automation challenge, done in August 2021.  

Technologies used:
- python3
- selenium
- pytest
- pytest-BDD
- pytest-html
- webDriver-manager
- faker 
- pipenv  

## Install PipEnv

To run the project, pipenv is recommended.

```Bash
    pip install pipenv
```  
  
All dependencies are available in Pipfile, run the command `pipenv install` on the project directory to install them.  

```Bash
    pipenv install
```

## Project Structure
The project structure is design to follow a *Page Object Model* and *BDD*.

```
.
|-- assets
|   `-- style.css
|-- tests
|   |-- features
|   |   `-- challenge.feature
|   |-- pages
|   |   |-- accountInfoPage.py
|   |   |-- basePage.py
|   |   |-- homePage.py
|   |   |-- __init__.py
|   |   |-- locators.py
|   |   |-- loginPage.py
|   |   `-- registerPage.py
|   |-- step_defs
|   |   |-- challenge_steps.py
|   |   `-- __init__.py
|   `-- test_challenge.py
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- report.html
`-- userData.json

```

### Run Project

To run the project, be sure to have install all dependencies with `pipenv`.
Once that is done, run:  

```Bash
    pipenv shell
```

and run pytest:  

```Bash
    pytest -v tests/test_challenge.py
```  

There's also the `pytest-html` module that can generate the report.  
To generate the report:

```Bash
    pytest -v tests/test_challenge.py --html=report.html
```
