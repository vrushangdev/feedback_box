import pytest
from mock import Mock
from typing import Tuple

from feedback_box.application.interfaces.icommand_query import CommandQuery
from feedback_box.application.inbox.queries.get_all import GetAllInboxesQuery


@pytest.fixture(scope='function')
def get_all_inboxes_query_with_mock_db(mock_db_service) -> Tuple[Mock, CommandQuery]:
    query = GetAllInboxesQuery(db=mock_db_service)

    return mock_db_service, query


class TestGetAllInboxesQuery:

    def test_get_all_inboxes_query_initialize_correctly(self, get_all_inboxes_query_with_mock_db):
        db, query = get_all_inboxes_query_with_mock_db

        assert isinstance(query, GetAllInboxesQuery)
        assert hasattr(query, 'db')
        assert query.db is db

    def test_get_all_inboxes_query_returns_empty_list(self):
        db = Mock()
        db.get_all_inboxes.return_value = []

        query = GetAllInboxesQuery(db=db)
        result = query.execute()

        assert result == []
        db.get_all_inboxes.assert_called_with()

    def test_get_all_inboxes_query_returns_list_of_inboxes(self, get_all_inboxes_query_with_mock_db):
        db, query = get_all_inboxes_query_with_mock_db

        result = query.execute()

        assert len(result) == 2
        db.get_all_inboxes.assert_called_with()
