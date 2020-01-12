import pytest
from flask import Flask

from feedback_box.service import create_app
from feedback_box.service.config import TestConfig


@pytest.fixture(scope='function')
def app() -> Flask:
    return create_app(config_object=TestConfig)
