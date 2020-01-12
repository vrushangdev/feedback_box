from typing import List

from feedback_box.domain.inbox import Inbox
from feedback_box.persistance.singleton_db import SingletonDb
from feedback_box.persistance.exceptions import NoMatchingInbox
from feedback_box.application.interfaces.idatabase_service import IDatabaseService


INBOX_DICT_KEYS = (
    'owner',
    'password',
    'question'
)


class MemoryDatabaseService(IDatabaseService, SingletonDb):
    data = None

    def __init__(self, data: List[dict] = None) -> None:
        if self.data is None:
            self.data = data or []

    def create_inbox(self, adict: dict) -> Inbox:
        for key in INBOX_DICT_KEYS:
            assert key in adict.keys()

        self.data.append(adict)

        return Inbox.from_dict(adict=adict)

    def get_all_inboxes(self) -> List[Inbox]:
        result = [
            Inbox.from_record(i) for i in self.data
        ]

        return result

    def find_inbox(self, inbox_id: str) -> Inbox:
        match = None

        for inbox in self.data:
            if inbox['id'] == inbox_id:
                match = inbox

        if match:
            return Inbox.from_record(match)
        else:
            raise NoMatchingInbox(f'No matching Inbox for id: {inbox_id}')
