import pytest
from mock import Mock
from uuid import uuid4
from typing import List

from feedback_box.domain.inbox import Inbox
from feedback_box.domain.tripcode import Tripcode


@pytest.fixture
def inbox() -> Inbox:
    return Inbox(
        owner='test_owner',
        password='dummy_password',
        question='Do you like me?'
    )


@pytest.fixture
def inboxes_data() -> List[dict]:
    inbox_1 = {
        'id': str(uuid4()),
        'owner': 'first_owner',
        'tripcode': Tripcode().generate_code(owner='first_owner', password='dummy_password'),
        'question': 'Do you like me?'
    }

    inbox_2 = {
        'id': str(uuid4()),
        'owner': 'second_owner',
        'tripcode': Tripcode().generate_code(owner='second_owner', password='dummy_password'),
        'question': 'Do you like icecream?'
    }

    return [
        inbox_1,
        inbox_2
    ]


@pytest.fixture(scope='function')
def mock_db_service(inbox: Inbox, inboxes_data: List[dict]) -> Mock:
    db = Mock()

    db.create_inbox.return_value = inbox
    db.get_all_inboxes.return_value = [
        Inbox.from_record(record) for record in inboxes_data
    ]
    db.find_inbox.return_value = inbox

    return db
