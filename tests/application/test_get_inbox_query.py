import pytest
from uuid import uuid4
from mock import Mock
from typing import Tuple

from feedback_box.application.inbox.queries.get import GetInboxQuery
from feedback_box.application.interfaces.icommand_query import CommandQuery


@pytest.fixture
def get_inbox_query_with_db(mock_db_service) -> Tuple[Mock, CommandQuery]:
    query = GetInboxQuery(mock_db_service)

    return mock_db_service, query


class TestGetInboxQuery:

    def test_get_inbox_query_initialize_correctly(self, get_inbox_query_with_db):
        db, query = get_inbox_query_with_db

        assert isinstance(query, GetInboxQuery)
        assert hasattr(query, 'db')
        assert query.db is db

    def test_get_inbox_query_returns_inbox_when_called_with_correct_id(self, inbox,
                                                                       get_inbox_query_with_db):
        db, query = get_inbox_query_with_db
        inbox_id = inbox.id

        result = query.execute(inbox_id=inbox_id)

        assert result == inbox
        db.find_inbox.assert_called_with(inbox_id)

    def test_get_inbox_query_throws_exception_when_no_inbox_was_found(self):
        db = Mock()
        db.find_inbox.side_effect = Exception

        query = GetInboxQuery(db=db)

        with pytest.raises(Exception):
            query.execute(inbox_id=str(uuid4()))
