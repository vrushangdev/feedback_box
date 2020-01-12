import pytest
from mock import Mock
from typing import Tuple

from feedback_box.application.interfaces.icommand_query import CommandQuery
from feedback_box.application.inbox.commands.create import CreateInboxCommand


@pytest.fixture(scope='function')
def inbox_create_command_with_mock_db(mock_db_service) -> Tuple[Mock, CommandQuery]:
    command = CreateInboxCommand(db=mock_db_service)

    return mock_db_service, command


class TestCreateInboxCommand:

    def test_create_inbox_command_initialize_correctly(self, inbox_create_command_with_mock_db):
        db, command = inbox_create_command_with_mock_db

        assert isinstance(command, CreateInboxCommand)
        assert hasattr(command, 'db')
        assert command.db is db

    def test_create_inbox_command_executes_correctly(self, inbox_create_command_with_mock_db):
        db, command = inbox_create_command_with_mock_db

        result = command.execute(
            owner='test_owner',
            password='dummy_password',
            question='Do you like me?'
        )

        db.create_inbox.assert_called_with(
            {
                'owner': 'test_owner',
                'password': 'dummy_password',
                'question': 'Do you like me?'
            }
        )
        assert result.owner == 'test_owner'
        assert result.question == 'Do you like me?'
