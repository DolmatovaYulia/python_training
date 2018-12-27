import pytest
from fixture.application import Application
import json
import os.path


fixture = None
target = None


@pytest.fixture
def app(request):
    # Инициализация. Создание фикстуры
    global fixture
    global target
    browser = request.config.getoption("--browser")
    # Проверка для предотвращения повторной загрузки конфигурационного файла
    if target is None:
        # Переменная __file__ содержит путь к файлу
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        # Читаем файл с помощью функции pytest_addoption
        with open(config_file) as f:
            # f содержит объект, который указывает на открытый файл
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        # функция создает объект класса Application
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_Login(user_name=target['user_name'], password=target['password'])
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
    parser.addoption("--target", action="store", default="target.json")

