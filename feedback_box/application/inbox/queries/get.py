from feedback_box.domain.inbox import Inbox
from feedback_box.application.interfaces.icommand_query import ICommandQuery
from feedback_box.application.interfaces.idatabase_service import DatabaseService


class GetInboxQuery(ICommandQuery):
    def __init__(self, db: DatabaseService) -> None:
        self.db = db

    def execute(self, inbox_id: str) -> Inbox:
        result = self.db.find_inbox(inbox_id)

        return result
