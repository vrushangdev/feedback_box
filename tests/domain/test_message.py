from datetime import datetime as dt
from uuid import UUID, uuid4

from feedback_box.domain.message import Message
from feedback_box.domain.tripcode import Tripcode, SEPARATOR, TRIPCODE_OWNER_INDEX


def create_sample_message(uuid: UUID = uuid4(), timestamp: dt = dt.now()) -> Message:
    return Message(
        inbox_id=uuid,
        tripcode=Tripcode().generate_code('test_author', 'dummy_password'),
        content='Hello! My name is Test Author!',
        timestamp=timestamp
    )


class TestMessageEntity:

    def test_message_initialize_correctly(self):
        uuid = uuid4()
        date = dt.now()

        message = create_sample_message(uuid=uuid, timestamp=date)

        assert message.inbox_id == uuid
        assert message.content == 'Hello! My name is Test Author!'
        assert message.timestamp == date

        assert isinstance(message.tripcode, Tripcode)

    def test_author_property_returns_message_author(self):
        message = create_sample_message()

        author = message.tripcode.code.split(SEPARATOR)[TRIPCODE_OWNER_INDEX]

        assert message.author == author
