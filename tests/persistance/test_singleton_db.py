import pytest

from feedback_box.persistance.singleton_db import SingletonDb


@pytest.fixture(scope='function')
def singleton_db() -> SingletonDb:
    yield SingletonDb()
    SingletonDb.clear_instances()


class TestSingletonDb:

    def test_singleton_db_creates_only_one_instance_of_itself(self, singleton_db):
        s_db = SingletonDb()

        assert s_db is singleton_db
        assert SingletonDb._instances[SingletonDb]

    def test_singleton_db_clears__instances_class_attribute(self):
        s_db = SingletonDb()
        SingletonDb.clear_instances()

        assert SingletonDb._instances == {}
