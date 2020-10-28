from prismaEDL import create_app
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config['DEBUG'] = True
    return app