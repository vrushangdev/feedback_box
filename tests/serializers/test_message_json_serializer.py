import json
import bcrypt
from uuid import uuid4
from datetime import datetime as dt

from feedback_box.domain.message import Message
from feedback_box.domain.tripcode import Tripcode
from feedback_box.serializers import message_json_serializer as ser


def test_serialize_message_entity(monkeypatch):
    monkeypatch.setattr(bcrypt, 'hashpw', lambda password, salt: 'hashed_password'.encode())

    inbox_id = uuid4()
    date = dt.now()

    message = Message(
        inbox_id=inbox_id,
        tripcode=Tripcode().generate_code('test_author', 'dummy_password'),
        content='Hello! This is a test content.',
        timestamp=date

    )
    json_inbox = json.dumps(message, cls=ser.MessageJsonEncoder)

    expected = f'''
        {{"inbox_id": "{inbox_id}",
        "tripcode": "test_author,hashed_password",
        "content": "Hello! This is a test content.",
        "timestamp": "{date.strftime(ser.TIMESTAMP_FORMAT)}"}}
    '''

    assert json.loads(json_inbox) == json.loads(expected)
