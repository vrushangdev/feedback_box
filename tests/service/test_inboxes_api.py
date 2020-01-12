import json
import mock
from uuid import uuid4

from feedback_box.domain.inbox import Inbox
from feedback_box.domain.tripcode import Tripcode


inbox_data = {
        'id': str(uuid4()),
        'owner': 'first_owner',
        'tripcode': Tripcode().generate_code(owner='first_owner', password='dummy_password'),
        'question': 'Do you like me?'
    }

inboxes = [
    Inbox.from_record(inbox_data)
]


class TestInboxesApi:

    @mock.patch('feedback_box.application.inbox.queries.get_all.GetAllInboxesQuery')
    def test_get_returns_list_of_inboxes(self, mock_query, client):
        mock_query().execute.return_value = inboxes

        http_response = client.get('/api/inboxes')

        assert json.loads(http_response.data.decode('UTF-8')) == [inbox_data]
        mock_query().execute.assert_called_with()
        assert http_response.status_code == 200
        assert http_response.mimetype == 'application/json'
