from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI
import pytest
from core.utils import get_db
from routes import routes
from typing import Any
from typing import Generator
from fastapi.testclient import TestClient


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


def start_application():
    app = FastAPI()
    app.include_router(routes)
    return app


SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionTest = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


CLEAN_TABLES = [
    "Menu",
    "Submenu",
    "Dish"
]


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTest, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTest(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(app: FastAPI, db_session: SessionTest) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def filled_menu():
    return {
        "id": 1,
        "title": "My test menu 1",
        "description": "My test menu description 1",
    }


@pytest.fixture(scope="function")
def filled_submenu():
    return {
        "id": 2,
        "menu_id": 1,
        "title": "My test submenu 1",
        "description": "My test submenu description 1",
    }


@pytest.fixture(scope="function")
def filled_dish():
    return {
        "id": 3,
        "submenu_id": 2,
        "title": "My test dish 1",
        "description": "My test dish description 1",
        "price": 11.11,
    }
