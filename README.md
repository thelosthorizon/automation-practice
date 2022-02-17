# Automation Practice Tests

Test major features/functionalities/user flows of Automation Practice Web app

## System Level Dependencies

* python 3.9.9
* python-pip 22.0.3
* virtualenv 20.13.1

## Things to keep in mind

### Test Planning

> I have used Google's ACC __(Attributes-Components-Capabilities)__ method to come up with the test plan. Capabilities = Test scenarios i.e. something we test for

> You can find the __color coded__ (based in risk matrix) high level test scenarios in the [test_plan](./test_plan.pdf). Note that there can be multiple tests within each test scenarios or a test can span across multiple scenarios

> Not all the test scenarios are covered. The ones that are not covered have either low risk profile or not relevant because the application is not designed for or I just ran out of time. The ones that are covered are automated

> Some of the tests might be flaky - probably not the best locator strategy used. This is in no way finalized and a lot of improvements can be made

### Automation Specific Things

> Not designed with portability in mind. Tested in __macOS Monterey 12.2__. Theoritically should work on a __linux distro__

> All the test files, pages and everything needed are located in __automation_practice__ directory

> Run all the commands from `root` directory i.e. `automation_practice`

> The tests are organized in layers following __Page Object Model__ (follows application structure closely). Tests do not touch locators directly. Most common part of the application is represented using pages. Layering means that the testcase is written in business vernacular. Layering also means re-usability, modularity and easier to maintain tests when things change and break

> configurations/pytest fixtures are defined in `conftest.py` both in `tests` directory which is shared by all the tests and also in individual test sub-packages within `tests` for e.g. `login` which contains `login` specific fixtures/configurations

> Three custom markers are defined `small` `medium` and `large` and is used to tage tests to capture both complexity/scope of a test. These tags can be used to select tests to run

> There is no need to install a WebDriver as a [WebDriver Manager](https://pypi.org/project/webdriver-manager/) is used to simiply handling of webdriver binaries

> Only explicit wait strategy is used (see why: [here](https://stackoverflow.com/questions/10404160/when-to-use-explicit-wait-vs-implicit-wait-in-selenium-webdriver)). The timeout (in seconds) can be set through `pytest` cli using `--timeout` option. This timeout will then be used by all the test functions that run. There are no custom conditions defined. We use the the utilities functions that are offered by selenium binding.


## Structure:

```
├── automation_practice
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── tests
|   |   ├── conftest.py
|   |   ├──login
|   |   |   ├── test_login.py
|   |   |   ├── conftest.py
|   |   |   ├── [....]
|   |   ├── [....]
│   ├── pages
|   |   ├── common
|   |   |   ├── headers
|   |   |   |   ├── navbar.py
|   |   |   |   ├── cart.py
|   |   |   |   ├── [....]
|   |   |   ├── [....]
|   |   ├── login
|   |   |   ├── login.py
|   |   |   ├── locators.py
|   |   |   ├── [....]
|   |   ├── [....]
├── README.md
├── test_plan.xmind
├── test_plan.pdf
├── .gitignore

```

## Steps

1. Install system dependencies

If you are on _macos_ you should have python 3.x already installed. For other platforms, you can install the dependencies above using suitable means, Google should take you long way. Install [ChromDriver](https://sites.google.com/chromium.org/driver/) of course you need to have chrome installed. ChromeDriver has to be in your PATH

2. Create and activate virtual environment [Virtualenv](https://virtualenv.pypa.io/en/latest/)

Run:
```
    pip3 install --user virtualenv
    virtualenv <name_of_virtual_env> --python=python3
    . <name_of_virtual_env>/bin/activate
```

If you dont have a python3 symlink, you can substitute full path instead. To deactivate just simply run `deactivate`

2. Install python dependencies
 ```pip install -r requirements.txt
 ```

3. Prepare reports directory

Its a good idea to create a directory called _reports_ where all the test reports from test runs run reside
 ```mkdir reports
 ```

4. Run the tests

Its probably a great idea to read a bit about [pytest](https://docs.pytest.org/en/7.0.x/) if you are not familiar with it. pytest comes with a nifty command line interface called `pytest` Run `pytest --help` to get all that `pytest` offers

```
pytest tests --html reports/report.html`
```
This will run all the tests and place a html report named __report.html__ in __reports__ directory. pytest makes it very easy to select tests based for e.g. based on markers. For e.g. the command below will only include tests with marker _small_ to be executed
```
pytest tests --html reports/report.html -m small --timeout 10`
```

Its also easy to select tests based on name (substring match). For e.g. the command below will only include tests that have _login_ in their name to be executed
```
pytest tests --html reports/report.html -k login --timeout 10`
```