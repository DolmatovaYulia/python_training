import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    # Initialization. Making fixtures
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        # функция создает объект класса Application
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_Login(user_name="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_Logout()
        fixture.Destroy()
    # How the fixture should be destroyed
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://addressbook/")

