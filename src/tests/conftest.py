import pytest
from src.api.models import *
from src import create_app, db  


@pytest.fixture(scope='module')
def test_app():
    app = create_app()  
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app  


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='function')
def add_user():
    def _add_user(name, last_name, email, user_type):
        user = User(name=name, last_name=last_name, email=email, user_type=user_type)
        db.session.add(user)
        db.session.commit()
        return user
    return _add_user