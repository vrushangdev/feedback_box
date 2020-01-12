from typing import Type
from flask import Flask
from flask_restful import Api

from feedback_box.service.config import Config, DevConfig
from feedback_box.service.inbox.inboxes_api import InboxesApi


def create_app(config_object: Type[Config] = DevConfig) -> Flask:
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config_object)
    register_resources(api)

    return app


def register_resources(api: Api) -> None:
    api.add_resource(InboxesApi, '/api/inboxes')
