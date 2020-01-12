from feedback_box.service import create_app
from feedback_box.service.config import DevConfig


app = create_app(config_object=DevConfig)
