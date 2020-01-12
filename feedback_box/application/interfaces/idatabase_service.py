import abc
from typing import List, NewType

from feedback_box.domain.inbox import Inbox


class IDatabaseService(abc.ABC):

    @abc.abstractmethod
    def create_inbox(self, adict: dict) -> Inbox:
        pass

    @abc.abstractmethod
    def get_all_inboxes(self) -> List[Inbox]:
        pass

    @abc.abstractmethod
    def find_inbox(self, inbox_id: str) -> Inbox:
        pass


DatabaseService = NewType('DatabaseService', IDatabaseService)
