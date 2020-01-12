import pytest
from uuid import UUID, uuid4

from feedback_box.domain.inbox import Inbox
from feedback_box.domain.tripcode import Tripcode


@pytest.fixture(scope='function')
def inbox() -> Inbox:
    return Inbox(
        owner='test_owner',
        password='dummy_password',
        question='Do you like me?'
    )


class TestInboxEntity:

    def test_inbox_initialize_correctly(self, inbox):
        assert isinstance(inbox, Inbox)

        assert hasattr(inbox, 'id')
        assert isinstance(inbox.id, UUID)

        assert inbox.owner == 'test_owner'
        assert inbox.question == 'Do you like me?'

        assert isinstance(inbox.tripcode, Tripcode)

    def test_creating_new_inbox_from_dict(self):
        dict_inbox = {
            'owner': 'test_owner',
            'password': 'dummy_password',
            'question': 'Do you like me?'
        }

        inbox = Inbox.from_dict(dict_inbox)

        assert isinstance(inbox, Inbox)

        assert hasattr(inbox, 'id')
        assert isinstance(inbox.id, UUID)

        assert inbox.owner == 'test_owner'
        assert inbox.question == 'Do you like me?'

        assert isinstance(inbox.tripcode, Tripcode)

    def test_creating_new_inbox_from_record(self):
        record_inbox = {
            'id': str(uuid4()),
            'owner': 'test_owner',
            'tripcode': Tripcode().generate_code('test_owner', 'dummy_password'),
            'question': 'Do you like me?'
        }

        inbox = Inbox.from_record(record_inbox)

        assert isinstance(inbox, Inbox)

        assert hasattr(inbox, 'id')
        assert isinstance(inbox.id, UUID)

        assert inbox.owner == 'test_owner'
        assert inbox.question == 'Do you like me?'

        assert isinstance(inbox.tripcode, Tripcode)

    def test_check_password_returns_true_when_called_with_correct_password(self, inbox):
        assert inbox.check_password('dummy_password')

    def test_check_password_returns_false_when_called_with_bad_password(self, inbox):
        assert not inbox.check_password('wrong_password')
