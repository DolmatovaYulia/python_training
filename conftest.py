import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    # Initialization. Making fixtures
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.Login(user_name="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.Login(user_name="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.Logout()
        fixture.Destroy()
    # How the fixture should be destroyed
    request.addfinalizer(fin)
    return fixture
