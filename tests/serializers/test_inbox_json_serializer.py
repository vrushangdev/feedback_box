import json
import bcrypt
from uuid import UUID, uuid4
from typing import Tuple

from feedback_box.domain.tripcode import Tripcode
from feedback_box.serializers import inbox_json_serializer as ser


def create_stub_inbox() -> Tuple[object, UUID]:
    inbox_id = uuid4()

    class StubInbox:
        def __init__(self):
            self.id = inbox_id
            self.owner = 'test_owner'
            self.tripcode = Tripcode()
            self.question = 'Do you like me?'

            self.tripcode.generate_code('test_owner', 'dummy_password')

    return StubInbox(), inbox_id


def test_serialize_inbox_entity(monkeypatch):
    monkeypatch.setattr(bcrypt, 'hashpw', lambda password, salt: 'hashed_password'.encode())

    stub_inbox, inbox_id = create_stub_inbox()
    json_inbox = json.dumps(stub_inbox, cls=ser.InboxJsonEncoder)

    expected = f'''
        {{"id": "{inbox_id}",
        "owner": "test_owner",
        "question": "Do you like me?",
        "tripcode": "test_owner,hashed_password"}}
    '''

    assert json.loads(json_inbox) == json.loads(expected)
