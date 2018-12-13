import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    # Initialization. Making fixtures
    fixture = Application()
    # How the fixture should be destroyed
    request.addfinalizer(fixture.Destroy)
    return fixture
