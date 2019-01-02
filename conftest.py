import pytest
from fixture.application import Application
from fixture.db import DBfixture
import json
import os.path
import importlib
import jsonpickle


fixture = None
target = None


# Функция, занимающаяся загрузкой конфигурации
def load_config(file):
    global target
    # Проверка для предотвращения повторной загрузки конфигурационного файла
    if target is None:
        # Переменная __file__ содержит путь к файлу
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        # Читаем файл с помощью функции pytest_addoption
        with open(config_file) as f:
            # f содержит объект, который указывает на открытый файл
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    # Инициализация. Создание фикстуры
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        # функция создает объект класса Application
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_Login(user_name=web_config['user_name'], password=web_config['password'])
    return fixture


# Фикстура для инициализации БД
@pytest.fixture(scope="session", autouse=True)
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DBfixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.Destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_Logout()
        fixture.Destroy()
    # How the fixture should be destroyed
    request.addfinalizer(fin)
    return fixture


# Отключаемая проверка
@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


# Фабрика тестов
def pytest_generate_tests(metafunc):
    # Получение информации о фикстурах, которые есть у тестовой функции (параметры)
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_form_module(fixture[5:])
            # Используем загруженные тестовые данные для того, чтобы параметризовать функцию
            # fixture - куда будут подставляться параметры
            # testdata - какие значения (источник данных)
            # ids - список со строковым представлением данных
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_form_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# Загружаем данные из модуля
def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata


# Загружаем данные из json-файла
def load_form_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        # Читаем данные и перекодируем обратно в исходный формат в виде объекта python
        return jsonpickle.decode(f.read())

