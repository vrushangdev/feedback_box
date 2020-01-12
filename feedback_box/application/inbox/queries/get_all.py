from typing import List

from feedback_box.domain.inbox import Inbox
from feedback_box.application.interfaces.icommand_query import ICommandQuery
from feedback_box.application.interfaces.idatabase_service import DatabaseService


class GetAllInboxesQuery(ICommandQuery):
    def __init__(self, db: DatabaseService) -> None:
        self.db = db

    def execute(self) -> List[Inbox]:
        inboxes = self.db.get_all_inboxes()

        return inboxes
