import pytest
from typing import List
from uuid import UUID, uuid4

from feedback_box.domain.inbox import Inbox
from feedback_box.domain.tripcode import Tripcode
from feedback_box.application.interfaces.idatabase_service import DatabaseService
from feedback_box.persistance.singleton_db import SingletonDb
from feedback_box.persistance.exceptions import NoMatchingInbox
from feedback_box.persistance.database_services.memory_database_service import MemoryDatabaseService


@pytest.fixture
def mem_db() -> DatabaseService:
    SingletonDb.clear_instances()
    yield MemoryDatabaseService()


@pytest.fixture(scope='function')
def mem_db_with_inboxes(inboxes_data: List[dict]) -> DatabaseService:
    SingletonDb.clear_instances()
    yield MemoryDatabaseService(inboxes_data)


class TestMemoryDatabaseService:

    def test_mem_db_initialize_correctly_without_data(self, mem_db):
        assert isinstance(mem_db, MemoryDatabaseService)
        assert hasattr(mem_db, 'data')
        assert mem_db.data == []

    def test_mem_db_initialize_correctly_with_data(self, mem_db_with_inboxes):
        assert isinstance(mem_db_with_inboxes.data, list)
        assert isinstance(mem_db_with_inboxes.data[0], dict)
        assert len(mem_db_with_inboxes.data) == 2

    def test_mem_db_creates_new_inbox(self, mem_db):
        inbox_data = {
            'owner': 'test_owner',
            'password': 'dummy_password',
            'question': 'Do you like me?'
        }

        mem_db.create_inbox(inbox_data)

        assert len(mem_db.data) == 1
        assert isinstance(mem_db.data[0], dict)

        assert mem_db.data[0]['owner'] == 'test_owner'
        assert mem_db.data[0]['question'] == 'Do you like me?'

    def test_mem_db_returns_empty_list_of_inboxes(self, mem_db):
        assert mem_db.get_all_inboxes() == []

    def test_mem_db_returns_list_of_inboxes(self, mem_db_with_inboxes):
        result = mem_db_with_inboxes.get_all_inboxes()

        assert len(result) == 2
        assert isinstance(result[0], Inbox)
        assert result[0].owner == 'first_owner'
        assert result[0].question == 'Do you like me?'

    def test_mem_db_finds_inbox_by_id(self, inboxes_data):
        inbox_id = inboxes_data[0]['id']

        SingletonDb.clear_instances()
        mem_db = MemoryDatabaseService(inboxes_data)

        result = mem_db.find_inbox(inbox_id=inbox_id)

        assert isinstance(result, Inbox)
        assert isinstance(result.tripcode, Tripcode)

        assert result.id == UUID(inbox_id)
        assert result.owner == 'first_owner'
        assert result.question == 'Do you like me?'

    def test_mem_db_throws_exception_when_no_inbox_was_found(self, mem_db_with_inboxes):
        with pytest.raises(NoMatchingInbox):
            mem_db_with_inboxes.find_inbox(str(uuid4()))
